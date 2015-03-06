# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('goalWeight', models.IntegerField(default=1, max_length=4)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('typeTask', models.CharField(default=b'NT', max_length=2, choices=[(b'NT', b'No type'), (b'LG', b'Leg'), (b'SH', b'Shoulder'), (b'CH', b'Chest')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tracker',
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
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.ManyToManyField(to='gym_app.Exercise')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='exercise',
            name='task',
            field=models.ManyToManyField(to='gym_app.Task'),
            preserve_default=True,
        ),
    ]
