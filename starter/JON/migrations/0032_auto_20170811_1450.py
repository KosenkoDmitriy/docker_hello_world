# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-08-11 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JON', '0031_vehicle_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='manufacturer_vehicle',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='manufacturer_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='model_name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
