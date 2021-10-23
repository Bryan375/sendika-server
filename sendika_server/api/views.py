from deepchem import feat
from deepchem.feat.base_classes import Featurizer
from django.shortcuts import render
from numpy.lib.npyio import load
from tensorflow.python.ops.gen_batch_ops import batch
from rest_framework import serializers, viewsets, status
from .serializers import MLSerializer
from .models import MLModel
from rest_framework.decorators import action
from rest_framework.response import Response

from deepchem.models.graph_models import GraphConvModel
from deepchem.feat import ConvMolFeaturizer
from deepchem.feat import MolGraphConvFeaturizer
from deepchem.data import JsonLoader
from deepchem.utils import UniversalNamedTemporaryFile
from deepchem.data import NumpyDataset
from deepchem.models.torch_models import AttentiveFPModel
import numpy as np
import matplotlib.pyplot as plt
import io
import pandas as pd
import models.GraphConv
import models.AttentiveFP
import os
import inspect


# Create your views here.
class MLView(viewsets.ModelViewSet):
    serializer_class = MLSerializer
    queryset = MLModel.objects.all()
    
    @action(methods=['post'], detail=False, url_path="predict-single-smile", url_name="predict_single_smile")
    def predictSingleSMILE(self, request):
        singleSmile = request.data
        serializers = MLSerializer(singleSmile, data=singleSmile)
            
        if serializers.is_valid():
            df = pd.DataFrame({'smile_name': [serializers.data.get('smile_name')], 'pIC50': 0.})

            with UniversalNamedTemporaryFile(mode="w") as tmpFile:
                df.to_json(tmpFile.name, orient='records', lines=True)

                if(serializers.data.get('model') == "GraphConvModel"):
                    featurizer = ConvMolFeaturizer()
                    loader = JsonLoader(['pIC50'], 'smile_name', featurizer)
                    inputSmile = loader.create_dataset(tmpFile.name)

                    checkpoint_path = models.GraphConv.__path__.__dict__["_path"][0]

                    transfered_model = GraphConvModel(n_tasks=1, 
                                                graph_conv_layers=[128, 64, 32],
                                                dense_layer_size=8,
                                                mode='regression', 
                                                dropout=0.4,
                                                number_atom_features=50,
                                                batch_size=256, 
                                                learning_rate=0.01, 
                                                batch_normalize=True,
                                                uncertainty=False,
                                                model_dir=checkpoint_path)
                                                
                else:
                    featurizer = MolGraphConvFeaturizer(use_edges=True)
                    train_smiles = df.loc[0, "smile_name"]
                    train_X = featurizer.featurize(train_smiles)
                    train_label = np.array(df.loc[0, "pIC50"])
                    train_label = np.reshape(train_label, (-1, 1))

                    inputSmile = NumpyDataset(X=train_X, y=train_label)

                    checkpoint_path = models.AttentiveFP.__path__.__dict__["_path"][0]

                    transfered_model = AttentiveFPModel(
                                            n_tasks=1, 
                                            num_layers=2,
                                            num_timesteps=2,
                                            graph_feat_size=32,
                                            dropout=0,
                                            mode='regression', 
                                            number_atom_features=30,
                                            number_bond_features=11,
                                            batch_size=100, 
                                            learning_rate=0.001, 
                                            self_loop=True,
                                            model_dir=checkpoint_path)

                transfered_model.restore()
                predicted_pIC50 = transfered_model.predict(inputSmile)

            return Response({"predicted_pIC50": predicted_pIC50[0][0]}, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)