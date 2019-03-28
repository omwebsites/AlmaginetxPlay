# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_track'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='title',
            field=models.TextField(verbose_name=b'title', blank=True),
        ),
    ]
