# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-10 00:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20170509_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='subservice',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nombre'),
        ),
    ]
