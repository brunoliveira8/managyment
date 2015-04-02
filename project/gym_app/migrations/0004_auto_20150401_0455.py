# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0003_auto_20150401_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodyscreening',
            name='abdominal',
            field=models.IntegerField(default=0, max_length=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bodyscreening',
            name='biceps',
            field=models.IntegerField(default=0, max_length=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bodyscreening',
            name='calf',
            field=models.IntegerField(default=0, max_length=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bodyscreening',
            name='chest',
            field=models.IntegerField(default=0, max_length=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bodyscreening',
            name='subscapular',
            field=models.IntegerField(default=0, max_length=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bodyscreening',
            name='suprailic',
            field=models.IntegerField(default=0, max_length=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bodyscreening',
            name='supraspinale',
            field=models.IntegerField(default=0, max_length=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bodyscreening',
            name='thigh',
            field=models.IntegerField(default=0, max_length=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bodyscreening',
            name='triceps',
            field=models.IntegerField(default=0, max_length=3),
            preserve_default=True,
        ),
    ]
