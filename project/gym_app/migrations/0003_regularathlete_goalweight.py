# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0002_remove_regularathlete_goalweight'),
    ]

    operations = [
        migrations.AddField(
            model_name='regularathlete',
            name='goalWeight',
            field=models.IntegerField(default=1, max_length=4),
            preserve_default=True,
        ),
    ]
