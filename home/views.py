from django.shortcuts import render
from .models import Pokemon, Ability, Type, Evolution
from django.core.paginator import Paginator
from django.db.models import Q

import pokebase as pb  # pip install pokebases
import random
import json


# Create your views here.
def home(request):
    pokemons = Pokemon.objects.all()

    end_index = pokemons.count()
    random_index = random.sample(range(1, end_index + 1), 12)

    random_cards = pokemons.filter(id__in=random_index)

    context = {
        'random_cards': random_cards
    }

    return render(request, 'home/home.html', context)

################ Card View ####################

def pokemon(request):
    #################### Use Only to fil the Database ######################
    # for i in range(startIndex, endIndex):
    #     item = Pokemon.objects.filter(id=i).exists()
    #     if item:
    #         # info = Pokemon.objects.get(id=i)
    #         continue
    #     else:
    #         get_info(i)
    ########################################################################

    pokemon = Pokemon.objects.prefetch_related('abilities', 'types')
    paginator = Paginator(pokemon, 20)
    pageNo = request.GET.get('page')
    pageObj = paginator.get_page(pageNo)
    
    # Checks if the last pokemon in the page is the last pokemon in the database
    last = Pokemon.objects.order_by('id').last()
    last_poke_id = pageObj[-1].id
    # print(last.slug)

########################################
    # if last_poke_id == last.id:
    #     call_get_info(last_poke_id)
########################################

    pokemon = Pokemon.objects.prefetch_related('abilities', 'types')
    paginator = Paginator(pokemon, 20)
    pageNo = request.GET.get('page')
    pageObj = paginator.get_page(pageNo)

    pokemon = pageObj.object_list

    context = {'pokemon': pokemon, 'page': pageObj, 'last': last_poke_id}
    return render(request, 'pokemon/pokemon.html', context)


def call_get_info(id=None):
    if id:
        startIndex = id + 1
    else:
        startIndex = 0
    endIndex = startIndex + 20
    for i in range(145, 201):
        get_info(i)
        print('created:', i)

def evolution(id=None, pokemon=None):
    if id:
        pokemon = pb.pokemon(id)
        poke = Pokemon.objects.get(id=id)
    else:
        name = pokemon.species.name
        poke = Pokemon.objects.get(name=name)
    evolutionChain = []
    chain = pokemon.species.evolution_chain.chain
    family = f"{chain.species.name}-family"

    evolution_chain(chain, evolutionChain)

    data = json.dumps({family: evolutionChain})

    evolve, _ = Evolution.objects.get_or_create(chain=data)

    poke.evolution_chain.add(evolve)
    print(family, 'added')

    

def evolution_chain(chain, evolutionChain):
    name = chain.species.name
    evolutionChain.append(name)  # Add the current Pokémon to the list of evolutions

    # Recursively get the evolutions of the current Pokémon
    for form in chain.evolves_to:
        evolution_chain(form, evolutionChain)


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
    info['image'] = f"https://github.com/PokeAPI/sprites/blob/master/sprites/pokemon/other/showdown/{poke_id}.gif?raw=true"
    # https://github.com/PokeAPI/sprites/blob/master/sprites/pokemon/other/showdown/25.gif?raw=true

    flavor = ""  # A single sentence to show in the card
    description = ""  # Full description to store in the database

    # Pokemon description
    species = pb.pokemon_species(pokemon.species.name)
    for entry in species.flavor_text_entries:
        text = entry.flavor_text
        if entry.language.name == 'en' and text not in description:
            if len(flavor) <= 1:
                flavor = text
            elif len(text) < len(flavor):
                flavor = text
            description += text

    info["flavor"] = flavor
    info["description"] = description
    
    save_info(info)
    evolution(pokemon=pokemon)

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
                    pokemon_img = info['image']
                )

    pokemon.save()
    abilities = info['abilities']
    for ability in abilities:
        ability, _ = Ability.objects.get_or_create(name=ability)
        # ability.save()
        pokemon.abilities.add(ability)
    
    types = info['types']
    for typ in types:
        typ, _ = Type.objects.get_or_create(name=typ)
        # typ.save()
        pokemon.types.add(typ)


############## Pokemon View ################

def pokemon_view(request, slug):
    
    pokemon = Pokemon.objects.get(slug=slug)
    id = pokemon.id
    poke_type = pokemon.types.all()
    related_pokemons = Pokemon.objects.filter(types__in=poke_type).exclude(id=id).distinct()
    
    evolutionChain = pokemon.evolution_chain.first()

    if evolutionChain:
        data = json.loads(evolutionChain.chain)

        family = next(iter(data))
        chain = data[family]
        # print(chain)

        evolution = Pokemon.objects.filter(name__in=chain)
    else:
        evolution = None


    context = {
        'pokemon': pokemon,
        'related_pokemons': related_pokemons,
        'evolution': evolution
    }
    return render(request, 'pokemon/pokemon_view.html', context)


def search(request):

    query = request.GET.get('query')
    pokemons = Pokemon.objects.all()

    try:
        id = int(query)
        pokemon = pokemons.filter(id__exact=id)
    except ValueError:
        pokemon = pokemons.filter(Q(name__icontains=query)|Q(types__name__icontains=query)).distinct()  # field in pokemon model __ field in related model __ lookup
    
    context = {
        "pokemons": pokemon,
        'query': query,
        'item': 'pokemon'
    }
    print(context)
    
    return render(request, 'home/search.html', context)


def about(request):

    return render(request, 'home/about.html')