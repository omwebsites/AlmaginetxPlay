# import your admin models here.
from django.contrib import admin

from .models import *

class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'create_at', 'slug')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nickname', 'password2', 'create_at', 'slug')

admin.site.register(Track, TrackAdmin)
admin.site.register(UserProfile, UserProfileAdmin)