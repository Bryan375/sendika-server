from django.shortcuts import render
from numpy.lib.npyio import load
from rest_framework import serializers, viewsets, status
from .serializers import MLSerializer
from .models import MLModel
from rest_framework.decorators import action
from rest_framework.response import Response

from deepchem.models.graph_models import GraphConvModel
from deepchem.feat import ConvMolFeaturizer
from deepchem.data import JsonLoader
from deepchem.utils import UniversalNamedTemporaryFile
import numpy as np
import matplotlib.pyplot as plt
import io
import pandas as pd



# Create your views here.
class MLView(viewsets.ModelViewSet):
    serializer_class = MLSerializer
    queryset = MLModel.objects.all()
    
    @action(methods=['post'], detail=False, url_path="predict-single-smile", url_name="predict_single_smile")
    def predictSingleSMILE(self, request):
        singleSmile = request.data
        serializers = MLSerializer(singleSmile, data=singleSmile)
        if serializers.is_valid():
            transfered_model = GraphConvModel(n_tasks=1, 
                                 graph_conv_layers=[256, 128, 64, 32, 1],
                                 dense_layer_size=512,
                                 mode='regression', 
                                 dropout=0.3,
                                 number_atom_features=75,
                                 batch_size=256, 
                                 learning_rate=0.001,
                                 batch_normalize=True)

            #transfered_model.restore()

            df = pd.DataFrame({'smile_name': [serializers.data.get('smile_name')], 'pIC50': 0.})
            with UniversalNamedTemporaryFile(mode="w") as tmpFile:
                df.to_json(tmpFile.name, orient='records', lines=True)
                featurizer = ConvMolFeaturizer()
                loader = JsonLoader(['pIC50'], 'smile_name', featurizer)
                inputSmile = loader.create_dataset(tmpFile.name)
            
            predicted_pIC50 = transfered_model.predict(inputSmile)

            return Response({"predicted_pIC50": predicted_pIC50[0][0]}, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)