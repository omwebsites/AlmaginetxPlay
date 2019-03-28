# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('audio', models.FileField(null=True, upload_to=b'tracks/audio', blank=True)),
                ('photo', models.FileField(null=True, upload_to=b'tracks/photo', blank=True)),
                ('publish', models.DateTimeField(auto_now_add=True, null=True)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=144, editable=False)),
                ('user', models.ForeignKey(related_name='track_user', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['create_at'],
                'verbose_name': 'Track',
                'verbose_name_plural': 'Tracks',
            },
        ),
    ]
