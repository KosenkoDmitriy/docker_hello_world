# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-08-08 20:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JON', '0026_auto_20170808_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='measure',
            field=models.CharField(choices=[('km', 'Kilometer(-s)'), ('kg', 'Kilogram(-s)'), ('h', 'Hour(-s)'), ('in', 'Inch(-es)'), ('ft', 'Foot(-s)'), ('yd', 'Yard(-s)'), ('mi', 'Mile(-s)'), ('oz', 'Ounce(-s)'), ('lb', 'Pound(-s)')], default='km', max_length=16),
        ),
    ]
