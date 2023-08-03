from django.contrib import admin

from .models import Pokemon, Type, Ability, Evolution

# Register your models here.
admin.site.register(Pokemon)
admin.site.register(Type)
admin.site.register(Ability)
admin.site.register(Evolution)