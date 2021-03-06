# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-25 23:44
from __future__ import unicode_literals

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to=main.models.profile_image_directory_path)),
                ('type', models.CharField(choices=[(0, 'Directivo'), (1, 'Cientifico'), (2, 'Tecnico')], max_length=1)),
            ],
        ),
    ]
