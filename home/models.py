from os import name
from django.db import models
from autoslug import AutoSlugField
import json

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        db_table = 'types'

    def __str__(self):
        return self.name

class Ability(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'abilities'

    def __str__(self):
        return self.name


class Evolution(models.Model):
    chain = models.JSONField()

    class Meta:
        ordering = ['pk']
        db_table = 'evolution'

    def __str__(self):

        data = json.loads(self.chain)
        name = next(iter(data))
        
        return name


class Pokemon(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    height = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    types = models.ManyToManyField(Type, related_name='pokemon_types')
    abilities = models.ManyToManyField(Ability, related_name='pokemon_abilities')
    stats = models.JSONField()
    description = models.TextField(max_length=100000, null=True)
    habitat = models.CharField(max_length=100, null=True)
    is_legendary = models.BooleanField(default=False)
    is_mythical = models.BooleanField(default=False)
    flavor = models.TextField(max_length=1000, null=True)

    evolution_chain = models.ManyToManyField(Evolution, related_name='pokemon_evolution_chain')

    pokemon_img = models.TextField(max_length=1000)

    # Add the custom method to generate the slug
    def generate_slug(self):
        return f'{self.name}-{self.id}'
    
    slug = AutoSlugField(populate_from=generate_slug, db_index=True)

    class Meta:
        ordering = ['id']
        db_table = 'pokemon'

    def __str__(self):
        return self.name


class Berry(models.Model):
    name = models.CharField(max_length=225)
    size = models.IntegerField()
    smoothness = models.IntegerField()
    soil_dryness = models.IntegerField()
    image = models.CharField(max_length=1000)
    growth_time = models.IntegerField()
    max_harvest = models.IntegerField()

    class Meta:
        ordering = ['id']
        db_table = 'berry'
        verbose_name = 'Berry'
        verbose_name_plural = 'Berries'

    def __str__(self):
        return f"{self.name}-berry"