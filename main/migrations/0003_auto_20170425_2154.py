# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-26 00:54
from __future__ import unicode_literals

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_person_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='type',
        ),
        migrations.AddField(
            model_name='person',
            name='area',
            field=models.CharField(choices=[(0, 'Directivo'), (1, 'Cientifico'), (2, 'Tecnico')], default=2, max_length=1, verbose_name='Tipo/Area'),
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(upload_to=main.models.profile_image_directory_path, verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last',
            field=models.CharField(max_length=30, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='person',
            name='position',
            field=models.CharField(default='', max_length=60, verbose_name='Cargo'),
        ),
    ]