# Generated by Django 3.1.14 on 2022-11-14 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0003_auto_20221114_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='photo',
            field=models.ImageField(null=True, upload_to='pokemon_pictures'),
        ),
    ]
