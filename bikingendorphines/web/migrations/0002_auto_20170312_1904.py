# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='height',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='weight',
            field=models.IntegerField(default=0),
        ),
    ]
