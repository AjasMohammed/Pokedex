from django.shortcuts import render
from .models import Pokemon, Ability, Type
from django.core.paginator import Paginator

import pokebase as pb  # pip install pokebases


# Create your views here.
def home(request):
    # info = get_info(25)
    last = Pokemon.objects.order_by('id').last()
    print(last)

    info_list = []
    for i in range(1, 21):
        item = Pokemon.objects.filter(id=i).exists()
        if item:
            info = Pokemon.objects.get(id=i)
        else:
            info = get_info(i)

        info_list.append(info)

    print(last)
    pokemon = Pokemon.objects.prefetch_related('abilities', 'types')

    paginator = Paginator(pokemon, 20)
    pageNo = request.GET.get('page')
    pageObj = paginator.get_page(pageNo)

    pokemon = pageObj.object_list

    context = {'pokemon': pokemon}
    return render(request, 'home/home.html', context)

def get_info(poke_id):
    info = {}
    pokemon = pb.pokemon(poke_id)

    info["name"] = pokemon.name
    info["id"] = pokemon.id
    info["height"] = pokemon.height
    info["weight"] = pokemon.weight
    info["types"] = [t.type.name for t in pokemon.types]
    info["abilities"] = [a.ability.name for a in pokemon.abilities]
    info["stats"] = {s.stat.name: s.base_stat for s in pokemon.stats}
    info['gif'] = f"https://github.com/PokeAPI/sprites/blob/master/sprites/pokemon/other/showdown/{poke_id}.gif?raw=true"
    # https://github.com/PokeAPI/sprites/blob/master/sprites/pokemon/other/showdown/25.gif?raw=true

    flavor = ""  # A single sentence to show in the card
    description = ""  # Full description to store in the database

    # Pokemon description
    species = pb.pokemon_species(pokemon.species.name)
    for entry in species.flavor_text_entries:
        text = entry.flavor_text
        if entry.language.name == 'en' and text not in flavor:
            if len(flavor) <= 1:
                flavor = text
            elif len(text) < len(flavor):
                flavor = text
            description += text

    info["flavor"] = flavor
    info["description"] = description
    print(info)
    print()

    save_info(info)
    return info


def save_info(info):

    pokemon = Pokemon(
                    id = info['id'],
                    name = info['name'],
                    height = info['height'],
                    weight = info['weight'],
                    stats = info['stats'],
                    flavor = info['flavor'],
                    description = info['description'],
                    pokemon_img = info['gif']
                )

    pokemon.save()
    abilities = info['abilities']
    for i in range(len(abilities)):
        ability = Ability(name=abilities[i])
        ability.save()
        pokemon.abilities.add(ability)
    
    types = info['types']
    for type in types:
        typ = Type(name=type)
        typ.save()
        pokemon.types.add(typ)

