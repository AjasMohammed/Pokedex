from os import name
from django.db import models
from autoslug import AutoSlugField
import json

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=100, unique=True)

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
    types = models.ManyToManyField(Type)
    abilities = models.ManyToManyField(Ability)
    stats = models.JSONField()
    description = models.TextField(max_length=100000, null=True)
    flavor = models.TextField(max_length=1000, null=True)

    evolution_chain = models.ManyToManyField(Evolution)

    pokemon_img = models.TextField(max_length=1000)

    # Add the custom method to generate the slug
    def generate_slug(self):
        return f'{self.name}-{self.id}'
    
    slug = AutoSlugField(populate_from=generate_slug)

    class Meta:
        ordering = ['id']
        db_table = 'pokemon'

    def __str__(self):
        return self.name

