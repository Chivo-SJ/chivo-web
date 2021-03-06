# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-10 00:59
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20170509_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='link',
            field=models.CharField(blank=True, max_length=400, null=True, validators=[django.core.validators.URLValidator()], verbose_name='Enlace'),
        ),
        migrations.AddField(
            model_name='subservice',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=main.models.service_image_directory_path, verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='image',
            field=models.ImageField(upload_to=main.models.institution_image_directory_path, verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='service',
            name='link',
            field=models.CharField(blank=True, max_length=400, null=True, validators=[django.core.validators.URLValidator()], verbose_name='Enlace'),
        ),
        migrations.AlterField(
            model_name='subservice',
            name='link',
            field=models.CharField(blank=True, max_length=400, null=True, validators=[django.core.validators.URLValidator()], verbose_name='Enlace'),
        ),
    ]
