# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0003_auto_20150305_0024'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='RegularAthlete',
        ),
    ]
