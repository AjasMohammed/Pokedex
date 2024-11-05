from django.contrib import admin

from .models import Pokemon, Type, Ability, Evolution, Berry

# Register your models here.
admin.site.register(Pokemon)
admin.site.register(Type)
admin.site.register(Ability)
admin.site.register(Evolution)
admin.site.register(Berry)