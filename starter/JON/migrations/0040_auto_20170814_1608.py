# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-08-14 16:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JON', '0039_remove_place_county'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='location',
            new_name='place',
        ),
    ]
