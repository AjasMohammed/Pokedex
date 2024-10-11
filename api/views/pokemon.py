from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from home.models import Pokemon
from api.serializers.pokemon import PokemonDetailSerializer
from django.core.paginator import Paginator
from api.pagination import CustomPagination, PaginationHandleMixin


class PokemonList(APIView, PaginationHandleMixin):
    pagination_class = CustomPagination
    serializer_class = PokemonDetailSerializer

    def get(self, request):
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
            "next_page": serializer.data['next'],
            "previous_page": serializer.data['previous'],
            "count": serializer.data['count'],
            "pokemons": serializer.data['results'].data,
        }
        return Response(context, status=status.HTTP_200_OK)


class PokemonDetail(APIView):
    def get(self, request, id):
        pokemon = get_object_or_404(Pokemon, id=id)
        serializer = PokemonDetailSerializer(pokemon)
        return Response(serializer.data, status=status.HTTP_200_OK)
