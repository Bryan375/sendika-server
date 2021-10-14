from rest_framework import serializers
from .models import MLModel

class MLSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLModel
        fields = '__all__'