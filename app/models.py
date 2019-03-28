# Create your models here.
# -*- encoding: utf-8 -*-
import uuid
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.utils.timezone import now
import os
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)
    nickname = models.CharField(blank=True, max_length=200, verbose_name="nickname")
    password2 = models.CharField(blank=True, max_length=200, verbose_name="Password")
    avatar = models.ImageField(upload_to='userprofiles/avatar', blank=True, null=True)
    create_at = models.DateTimeField(default=now, editable=False)
    update_at = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=True)
    class Meta:
        verbose_name = 'Userprofile'
        verbose_name_plural = 'Userprofiles'
    def __str__(self):
        return self.nickname
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.nickname)
        super(UserProfile, self).save(*args, **kwargs)

#Tracks

class Track(models.Model):
    title = models.TextField(blank=True, verbose_name="title")
    audio = models.FileField(upload_to='tracks/audio', blank=True, null=True)
    user = models.ForeignKey(User, related_name='track_user', blank=True, null=True)
    create_at = models.DateTimeField(default=now, editable=False)
    update_at = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=False,max_length=144)

    def get_absolute_url(self):
        return reverse('blog.track', kwargs={'slug': self.slug})

    def extension_class(self):
        name, extension = os.path.splitext(self.audio.name)
        return extension

    class Meta:
            ordering = ['create_at']
            verbose_name = 'Track'
            verbose_name_plural = 'Tracks'

    def __unicode__(self):
        return self.title

    def save(self):
        super(Track, self).save()
        date = self.create_at
        self.slug = '%i-%i-%i-audio-%i' % (
            date.year, date.month, date.day, self.id
        )
        super(Track, self).save()