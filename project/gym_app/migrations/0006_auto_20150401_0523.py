# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0005_auto_20150401_0510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodyscreening',
            name='result',
            field=models.CharField(default=b'Excellent', max_length=20, choices=[(b'Excellent', b'Excellent'), (b'Good', b'Good'), (b'Average', b'Average'), (b'Below Average', b'Below Average'), (b'Poor', b'Poor')]),
            preserve_default=True,
        ),
    ]
