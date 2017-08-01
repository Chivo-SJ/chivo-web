# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-26 01:38
from __future__ import unicode_literals

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20170425_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='last',
        ),
        migrations.AlterField(
            model_name='person',
            name='area',
            field=models.CharField(choices=[('0', 'Directivo'), ('1', 'Cientifico'), ('2', 'Tecnico')], max_length=1, verbose_name='Tipo/Area'),
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=main.models.profile_image_directory_path, verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=60, verbose_name='Nombre'),
        ),
    ]