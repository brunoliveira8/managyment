# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0007_bodyscreening_bodyfat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bodyscreening',
            name='result',
        ),
    ]
