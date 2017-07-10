# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 01:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeometricModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='GeometricModel')),
            ],
        ),
        migrations.CreateModel(
            name='Limits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minlon', models.FloatField()),
                ('minlat', models.FloatField()),
                ('maxlon', models.FloatField()),
                ('maxlat', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='MechanicalInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bs_t', models.FloatField()),
                ('Bs_c', models.FloatField()),
                ('e', models.FloatField()),
                ('R', models.FloatField()),
                ('mx_s', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Resolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geo_delta', models.FloatField()),
                ('z_delta', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='RheologicModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('H', models.FloatField()),
                ('n', models.FloatField()),
                ('A', models.FloatField()),
                ('ref', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ThermalInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('K_z', models.BooleanField(verbose_name='K = f(z)')),
                ('H_z', models.BooleanField(verbose_name='H = f(z)')),
                ('EF_lat', models.BooleanField(verbose_name='EF = f(lat)')),
                ('EF', models.FloatField(verbose_name='EF: edad de la corteza oceanica en la fosa (Ma)')),
                ('K_cs', models.FloatField(verbose_name='K(cs): conductividad termica corteza sup. (W/mK)')),
                ('K_ci', models.FloatField(verbose_name='K(ci): conductividad termica corteza inf. (W/mK)')),
                ('K_ml', models.FloatField(verbose_name='K(ml): conductividad termica manto litosferico (W/mK)')),
                ('H_cs', models.FloatField(verbose_name='H(cs): calor radiogenico corteza sup. (W/m3)')),
                ('H_ci', models.FloatField(verbose_name='H(ci): calor radiogenico corteza inf. (W/m3)')),
                ('H_ml', models.FloatField(verbose_name='H(ml): calor radiogenico manto litosferico (W/m3)')),
                ('kpa', models.FloatField(verbose_name='kpa: difusividad termica (m2/s)')),
                ('T_p', models.FloatField(verbose_name='Tp: temperatura potencial del manto (C)')),
                ('G_a', models.FloatField(verbose_name='Ga: gradiente adiabatico (K/m)')),
                ('V', models.FloatField(verbose_name='V: velocidad de convergencia (m/Ma)')),
                ('b', models.FloatField(verbose_name='b: parametro adimensional')),
                ('dip', models.FloatField(verbose_name='dip: angulo de subduccion')),
                ('D2', models.FloatField(verbose_name='D2: constante de proporcionalidad adimensional')),
                ('d_rad', models.FloatField(verbose_name='Drad: decaimiento radiogenico (km)')),
            ],
        ),
        migrations.CreateModel(
            name='TrenchAge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('age', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='mechanicalinput',
            name='Ci',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ci', to='matrices.RheologicModel'),
        ),
        migrations.AddField(
            model_name='mechanicalinput',
            name='Cs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cs', to='matrices.RheologicModel'),
        ),
        migrations.AddField(
            model_name='mechanicalinput',
            name='Ml',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ml', to='matrices.RheologicModel'),
        ),
    ]