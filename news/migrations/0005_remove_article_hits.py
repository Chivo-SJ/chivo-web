# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-01 04:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_article_hits'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='hits',
        ),
    ]