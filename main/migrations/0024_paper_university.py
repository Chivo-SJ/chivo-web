# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-02 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20170601_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='university',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Universidad'),
        ),
    ]