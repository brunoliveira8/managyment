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
