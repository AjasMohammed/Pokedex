from django.shortcuts import render
import pokebase as pb


# Create your views here.
def home(request):
    info = get_info(25)
    return render(request, 'home/home.html', info)

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

    description = ""

    # Pokemon description
    species = pb.pokemon_species(pokemon.species.name)
    for entry in species.flavor_text_entries:
        if entry.language.name == 'en' and entry.flavor_text not in description:
            description += entry.flavor_text
    info["description"] = description

    return info
