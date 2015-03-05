# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0004_auto_20150305_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='typeTask',
            field=models.CharField(default=b'NT', max_length=2, choices=[(b'NT', b'No type'), (b'LG', b'Leg'), (b'SH', b'Shoulder'), (b'CH', b'Chest')]),
            preserve_default=True,
        ),
    ]
