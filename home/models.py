from os import name
from django.db import models

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Ability(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


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

    pokemon_img = models.ImageField(upload_to='pokemon')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

