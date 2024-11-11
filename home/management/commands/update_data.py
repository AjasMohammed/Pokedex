from django.core.management.base import BaseCommand
import pokebase as pb
from home.models import Pokemon


class Command(BaseCommand):
    help = "Loads data from pokabase API to the Database."

    def handle(self, *args, **kwargs) -> str | None:
        pokemons = Pokemon.objects.filter(id__gte=386)

        for pokemon in pokemons:
            pk = pb.pokemon(pokemon.id)
            specie = pk.species
            if specie.habitat:
                habitat = specie.habitat.name
            else:
                habitat = None

            pokemon.habitat = habitat
            pokemon.is_legendary = specie.is_legendary
            pokemon.is_mythical = specie.is_mythical

            pokemon.save()
            print(f'UPDATED {pokemon.name} - {pokemon.id}')