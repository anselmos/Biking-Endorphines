# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 21:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20170312_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(default=0.0)),
                ('lon', models.FloatField(default=0.0)),
                ('elevation', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_name', models.CharField(max_length=100)),
                ('avg_route', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='RoutePoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Point')),
                ('id_route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Route')),
            ],
        ),
        migrations.CreateModel(
            name='UserRoute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Route')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='surname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='userroute',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.User'),
        ),
    ]
