# Generated by Django 4.2.3 on 2023-07-30 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_pokemon_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='types',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]
