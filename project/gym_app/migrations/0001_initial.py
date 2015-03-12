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
                ('weight', models.IntegerField(default=1, max_length=4)),
                ('repetition', models.IntegerField(default=1, max_length=4)),
                ('sets', models.IntegerField(default=1, max_length=4)),
                ('day', models.IntegerField(default=1, max_length=7, choices=[(1, b'Day 1'), (2, b'Day 2'), (3, b'Day 3'), (4, b'Day 4'), (5, b'Day 5'), (6, b'Day 6'), (7, b'Day 7')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RegularAthlete',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goal_weight', models.IntegerField(default=1, max_length=4)),
                ('level', models.CharField(default=b'BG', max_length=2, choices=[(b'BG', b'Begginer'), (b'IN', b'Intermediate'), (b'AD', b'Advanced')])),
                ('training_period', models.CharField(default=b'MO', max_length=2, choices=[(b'MO', b'Morning'), (b'AF', b'Afternoon'), (b'NI', b'Night')])),
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
            name='WorkoutPlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exercises', models.ManyToManyField(to='gym_app.Exercise')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='regularathlete',
            name='workout_plan',
            field=models.OneToOneField(to='gym_app.WorkoutPlan'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exercise',
            name='task',
            field=models.ForeignKey(to='gym_app.Task'),
            preserve_default=True,
        ),
    ]
