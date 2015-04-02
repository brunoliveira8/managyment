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
            name='BodyScreening',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('screeningDate', models.DateField(auto_now_add=True)),
                ('triceps', models.DecimalField(default=0, max_digits=5, decimal_places=2)),
                ('biceps', models.DecimalField(default=0, max_digits=5, decimal_places=2)),
                ('subscapular', models.DecimalField(default=0, max_digits=5, decimal_places=2)),
                ('supraspinale', models.DecimalField(default=0, max_digits=5, decimal_places=2)),
                ('suprailic', models.DecimalField(default=0, max_digits=5, decimal_places=2)),
                ('abdominal', models.DecimalField(default=0, max_digits=5, decimal_places=2)),
                ('chest', models.DecimalField(default=0, max_digits=5, decimal_places=2)),
                ('thigh', models.DecimalField(default=0, max_digits=5, decimal_places=2)),
                ('calf', models.DecimalField(default=0, max_digits=5, decimal_places=2)),
                ('weight', models.IntegerField(default=0, max_length=4)),
                ('feet', models.IntegerField(default=0, max_length=4)),
                ('inches', models.IntegerField(default=0, max_length=4)),
                ('result', models.CharField(default=b'EX', max_length=2, choices=[(b'EX', b'Excellent'), (b'GO', b'Good'), (b'AV', b'Average'), (b'BA', b'Below Average'), (b'PO', b'Poor')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
            name='PersonalTrainer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.CharField(default=b'M', max_length=2, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RegularAthlete',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.CharField(default=b'BG', max_length=2, choices=[(b'BG', b'Begginer'), (b'IN', b'Intermediate'), (b'AD', b'Advanced')])),
                ('training_period', models.CharField(default=b'MO', max_length=2, choices=[(b'MO', b'Morning'), (b'AF', b'Afternoon'), (b'NI', b'Night')])),
                ('gender', models.CharField(default=b'M', max_length=2, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('screenings', models.ManyToManyField(to='gym_app.BodyScreening')),
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
                ('startWeightDate', models.DateField(auto_now_add=True)),
                ('startWeight', models.IntegerField(default=0, max_length=4)),
                ('previousWeightDate', models.DateField(auto_now=True)),
                ('previousWeight', models.IntegerField(default=0, max_length=4)),
                ('currentWeightDate', models.DateField(auto_now=True)),
                ('currentWeight', models.IntegerField(default=170, max_length=4)),
                ('goalWeight', models.IntegerField(default=160, max_length=4)),
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
            name='tracker',
            field=models.OneToOneField(to='gym_app.Tracker'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='regularathlete',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
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
