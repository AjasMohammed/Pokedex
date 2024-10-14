from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from home.models import Pokemon
from api.serializers.pokemon import PokemonDetailSerializer
from api.pagination import CustomPagination, PaginationHandleMixin

import random


class PokemonList(APIView, PaginationHandleMixin):
    pagination_class = CustomPagination
    serializer_class = PokemonDetailSerializer

    def get(self, request):
        limit = request.GET.get('limit')
        if limit:
            pokemon_count = Pokemon.objects.count()
            random_ids = random.sample(range(1, pokemon_count), int(limit))
            pokemons = Pokemon.objects.filter(id__in=random_ids).prefetch_related(
                'types', 'abilities', 'evolution_chain')[:int(limit)]
            serializer = self.serializer_class(pokemons, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            pokemons = Pokemon.objects.all().prefetch_related(
                'types', 'abilities', 'evolution_chain')
            serializer = self.serializer_class(pokemons, many=True)
            page = self.paginate_queryset(pokemons)
            if page is not None:
                serializer = self.get_paginated_response(
                    self.serializer_class(page, many=True))
            else:
                serializer = self.serializer_class(pokemons, many=True)

            context = {
                "next_page": serializer.data.get('next', None),
                "previous_page": serializer.data.get('previous', None),
                "count": serializer.data.get('count', None),
                "pokemons": serializer.data.get('results', None).data,
            }
            return Response(context, status=status.HTTP_200_OK)


class PokemonDetail(APIView):
    def get(self, request, id):
        pokemon = get_object_or_404(Pokemon, id=id)
        serializer = PokemonDetailSerializer(pokemon)
        return Response(serializer.data, status=status.HTTP_200_OK)
