from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('pokemon', views.pokemon),
    path('pokemon/<slug:slug>', views.pokemon_view, name='pokemon_view'),
]
