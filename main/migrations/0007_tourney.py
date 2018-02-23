# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-22 00:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_location_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tourney',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('machine', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
    ]
