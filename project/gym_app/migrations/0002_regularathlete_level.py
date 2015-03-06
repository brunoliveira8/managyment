# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='regularathlete',
            name='level',
            field=models.CharField(default=b'BG', max_length=2, choices=[(b'BG', b'Begginer'), (b'IN', b'Intermediate'), (b'AD', b'Advanced')]),
            preserve_default=True,
        ),
    ]
