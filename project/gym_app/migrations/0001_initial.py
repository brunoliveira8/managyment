# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.IntegerField(max_length=4)),
                ('repetition', models.IntegerField(max_length=4)),
                ('sets', models.IntegerField(max_length=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RegularAthlete',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstName', models.CharField(max_length=32)),
                ('lastName', models.CharField(max_length=32)),
                ('username', models.CharField(unique=True, max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=64)),
                ('goalWeight', models.IntegerField(max_length=4)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('typeTask', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WeightProgress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('startDate', models.DateField(auto_now_add=True)),
                ('startWeight', models.IntegerField(max_length=4)),
                ('previousDate', models.DateField()),
                ('previousWeight', models.IntegerField(max_length=4)),
                ('lastDate', models.DateField(auto_now=True)),
                ('lastWeight', models.IntegerField(max_length=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
