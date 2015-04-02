# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0004_auto_20150401_0455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodyscreening',
            name='result',
            field=models.CharField(default=b'Excellent', max_length=2, choices=[(b'Excellent', b'Excellent'), (b'GO', b'Good'), (b'AV', b'Average'), (b'BA', b'Below Average'), (b'PO', b'Poor')]),
            preserve_default=True,
        ),
    ]
