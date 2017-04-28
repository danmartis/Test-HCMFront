# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 02:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sala',
            name='insumos',
        ),
        migrations.AddField(
            model_name='sala',
            name='insumos',
            field=models.ManyToManyField(to='reserva.Insumo'),
        ),
    ]