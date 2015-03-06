# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0002_regularathlete_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='regularathlete',
            name='training_period',
            field=models.CharField(default=b'MO', max_length=2, choices=[(b'MO', b'Morning'), (b'AF', b'Afternoon'), (b'NI', b'Night')]),
            preserve_default=True,
        ),
    ]
