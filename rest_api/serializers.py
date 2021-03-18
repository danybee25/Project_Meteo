from rest_framework import serializers
from .models import MountainData


class MountainDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MountainData
        fields = '__all__'
