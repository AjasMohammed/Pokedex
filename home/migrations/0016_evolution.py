# Generated by Django 4.2.3 on 2023-08-03 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_ability_name_alter_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evolution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chain', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
