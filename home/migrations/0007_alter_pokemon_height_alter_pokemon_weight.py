# Generated by Django 4.2.3 on 2023-07-30 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_type_remove_pokemon_type_pokemon_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
