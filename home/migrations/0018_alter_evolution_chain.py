# Generated by Django 4.2.3 on 2023-08-03 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_pokemon_evolution_chain_alter_evolution_chain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evolution',
            name='chain',
            field=models.JSONField(),
        ),
    ]
