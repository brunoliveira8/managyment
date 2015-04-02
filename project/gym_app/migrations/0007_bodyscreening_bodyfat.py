# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0006_auto_20150401_0523'),
    ]

    operations = [
        migrations.AddField(
            model_name='bodyscreening',
            name='bodyfat',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
    ]
