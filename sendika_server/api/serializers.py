from rest_framework import serializers
from .models import MLModel

class MLSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLModel
        fields = ('id', 'smile_name', 'result')