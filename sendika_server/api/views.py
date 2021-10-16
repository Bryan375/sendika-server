from django.shortcuts import render
from rest_framework import serializers, viewsets, status
from .serializers import MLSerializer
from .models import MLModel
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class MLView(viewsets.ModelViewSet):
    serializer_class = MLSerializer
    queryset = MLModel.objects.all()
    
    
    @action(methods=['post'], detail=False, url_path="predict-single-smile", url_name="predict_single_smile")
    def predictSingleSMILE(self, request):
        singleSmile = request.data
        print(singleSmile)
        serializers = MLSerializer(singleSmile, data=singleSmile)
        if serializers.is_valid():
            
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)