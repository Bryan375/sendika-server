from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MLSerializer
from .models import MLModel

# Create your views here.
class MLView(viewsets.ModelViewSet):
    serializer_class = MLSerializer
    queryset = MLModel.objects.all()