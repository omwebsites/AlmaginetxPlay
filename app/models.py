# Create your models here.
# -*- encoding: utf-8 -*-
import uuid
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.utils.timezone import now
from blog.models import *
import os
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)
    username = models.CharField(blank=True, max_length=200, verbose_name="Username")
    password = models.CharField(blank=True, max_length=200, verbose_name="Password")
    avatar = models.ImageField(upload_to='userprofiles/avatar', blank=True, null=True)
    create_at = models.DateTimeField(default=now, editable=False)
    update_at = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=False)
    class Meta:
        verbose_name = 'Userprofile'
        verbose_name_plural = 'Userprofiles'
    def __str__(self):
        return self.user.username
    def extension_class(self):
        username, extension = os.path.splitext(self.archive.username)
        return extension
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)