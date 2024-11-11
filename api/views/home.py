from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from home.models import Pokemon, Berry, Evolution
from api.serializers.pokemon import PokemonDetailSerializer
from api.serializers.berry import BerrySerializer

import random


class HomePageAPI(APIView):
    def get(self, request):
        limit = 6

        # POKEMON DATA
        pokemon_data = Pokemon.objects.all().prefetch_related('types', 'abilities', 'evolution_chain')
        pokemon_count = pokemon_data.count()
        random_ids = random.sample(range(1, pokemon_count), int(limit))
        pokemons = pokemon_data.filter(id__in=random_ids)
        pokemon_serializer = PokemonDetailSerializer(pokemons, many=True)

        # EVOLUTION DATA
        pokemon_evolution = pokemon_data.filter(evolution_chain=pokemons.first().evolution_chain.first())
        evolution_serializer = PokemonDetailSerializer(pokemon_evolution, many=True)

        # BERRY DATA
        random_ids = random.sample(range(1, 64), 10)
        berries = Berry.objects.filter(id__in=random_ids)
        berry_serializer = BerrySerializer(berries, many=True)

        context = {
            'pokemon': pokemon_serializer.data,
            'evolution': evolution_serializer.data,
            'berries': berry_serializer.data,
        }

        return Response(context, status=status.HTTP_200_OK)
