# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0009_bodyscreening_bmi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodyscreening',
            name='bmi',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=1),
            preserve_default=True,
        ),
    ]
