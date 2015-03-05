# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='task',
            field=models.ManyToManyField(to='gym_app.Task'),
            preserve_default=True,
        ),
    ]
