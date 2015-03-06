# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0003_regularathlete_training_period'),
    ]

    operations = [
        migrations.RenameField(
            model_name='regularathlete',
            old_name='goalWeight',
            new_name='goal_weight',
        ),
    ]
