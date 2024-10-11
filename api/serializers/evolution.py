from rest_framework import serializers 
from home.models import Evolution


class EvolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evolution
        fields = '__all__'