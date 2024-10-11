from rest_framework import serializers
from home.models import Pokemon
from .type import TypeSerializer
from .ability import AbilitySerializer
from .evolution import EvolutionSerializer



class PokemonDetailSerializer(serializers.ModelSerializer):
    types = TypeSerializer(many=True)
    abilities = AbilitySerializer(many=True)
    evolution_chain = EvolutionSerializer(many=True)
    class Meta:
        model = Pokemon
        fields = '__all__'