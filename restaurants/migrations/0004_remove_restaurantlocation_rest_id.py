# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 07:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_restaurantlocation_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurantlocation',
            name='rest_id',
        ),
    ]
