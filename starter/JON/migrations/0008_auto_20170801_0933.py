# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-08-01 09:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JON', '0007_auto_20170801_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordertype',
            name='delivery_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ordertype',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ordertype',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='condition',
            name='measure',
            field=models.CharField(choices=[('km', 'Kilometer'), ('kg', 'Kilogram'), ('h', 'Hour(-s)')], default='km', max_length=16),
        ),
        migrations.AlterField(
            model_name='orderstatus',
            name='name',
            field=models.CharField(choices=[(0, 'Drafted'), (1, 'Created'), (2, 'Ordered'), (3, 'En Route'), (4, 'Completed')], default=0, max_length=16),
        ),
        migrations.AlterField(
            model_name='ordertype',
            name='name',
            field=models.CharField(choices=[(0, 'None'), (1, 'Subscription'), (2, 'Overnight'), (3, 'Day Delivery'), (4, 'Hotshot')], default=0, max_length=32),
        ),
    ]