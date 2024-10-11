from django.urls import path
from . import views

urlpatterns = [
    path('pokemon/', views.PokemonList.as_view()),
    path('pokemon/<int:id>', views.PokemonDetail.as_view()),
]