# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190325_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='track',
            name='publish',
        ),
    ]
