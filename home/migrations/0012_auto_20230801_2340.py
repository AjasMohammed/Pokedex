# Generated by Django 4.2.3 on 2023-08-01 18:10

from django.db import migrations
from autoslug.utils import slugify

def update_pokemon_slug(apps, schema_editor):
    pokemons = apps.get_model('home', 'Pokemon')
    for pokemon in pokemons.objects.all():
        pokemon.slug = slugify(f'{pokemon.name}-{pokemon.id}')
        pokemon.save()

class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_pokemon_slug'),
    ]

    operations = [
    ]
