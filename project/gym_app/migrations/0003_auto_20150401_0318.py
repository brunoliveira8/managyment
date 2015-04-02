# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0002_auto_20150401_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodyscreening',
            name='screeningDate',
            field=models.DateField(default=datetime.datetime.now),
            preserve_default=True,
        ),
    ]
