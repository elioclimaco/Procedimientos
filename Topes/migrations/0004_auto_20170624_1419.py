# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-24 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Topes', '0003_auto_20170623_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='objetocontratacion',
            name='operador',
        ),
        migrations.AddField(
            model_name='objetocontratacion',
            name='operador_final',
            field=models.CharField(choices=[('MYRI', '>='), ('MYRQ', '>'), ('MNRI', '<='), ('MNRQ', '>'), ('IUAL', '=')], default='MYRI', max_length=50),
        ),
        migrations.AddField(
            model_name='objetocontratacion',
            name='operador_inicial',
            field=models.CharField(choices=[('MYRI', '>='), ('MYRQ', '>'), ('MNRI', '<='), ('MNRQ', '>'), ('IUAL', '=')], default='MYRI', max_length=50),
        ),
        migrations.AlterField(
            model_name='objetocontratacion',
            name='descripcion',
            field=models.CharField(choices=[('BIEN', 'Bienes'), ('SERV', 'Servicios'), ('OBRA', 'Obras')], max_length=200),
        ),
        migrations.AlterField(
            model_name='objetocontratacion',
            name='monto_final',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='objetocontratacion',
            name='monto_inicial',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]
