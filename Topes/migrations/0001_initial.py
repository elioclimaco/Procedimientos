# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoProcedimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=100)),
            ],
        ),
    ]