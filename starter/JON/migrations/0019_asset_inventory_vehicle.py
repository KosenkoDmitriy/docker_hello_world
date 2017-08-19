# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-08-08 11:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('JON', '0018_auto_20170808_1020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=64)),
                ('text', models.TextField(blank=True, default='')),
                ('type', models.CharField(choices=[('CP', 'Capital'), ('GD', 'Good')], default='CP', max_length=2)),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JON.Account')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=64)),
                ('text', models.TextField(blank=True, default='')),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JON.Asset')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=64)),
                ('text', models.TextField(blank=True, default='')),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JON.Asset')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
