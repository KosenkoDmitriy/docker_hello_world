# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-08-01 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JON', '0009_auto_20170801_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderstatus',
            name='name',
            field=models.IntegerField(choices=[(1, 'Drafted'), (2, 'Created'), (3, 'Ordered'), (4, 'En Route'), (5, 'Completed')], default=1, max_length=16),
        ),
    ]