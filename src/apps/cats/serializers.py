import requests

from rest_framework import serializers
from .models import SpyCat


class SpyCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = '__all__'

    def validate_breed(self, value):
        response = requests.get("https://api.thecatapi.com/v1/breeds")
        breeds = [breed['name'] for breed in response.json()]
        if value not in breeds:
            raise serializers.ValidationError(f"Invalid breed: {value}")
        return value
