# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-08-08 15:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('JON', '0023_delete_orderstatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='vehicle',
        ),
        migrations.AddField(
            model_name='order',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='JON.Driver'),
        ),
        migrations.AddField(
            model_name='order',
            name='vehicle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='JON.Vehicle'),
        ),
    ]
