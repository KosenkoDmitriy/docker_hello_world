# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-08-08 13:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JON', '0020_auto_20170808_1241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='driver',
        ),
    ]
