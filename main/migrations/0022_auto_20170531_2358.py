# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-01 03:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20170531_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='subservice',
            name='index',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Indice de Ordenamiento'),
        ),
        migrations.AlterField(
            model_name='service',
            name='index',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Indice de Ordenamiento'),
        ),
    ]
