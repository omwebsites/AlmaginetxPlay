# Create your urls here.
from django.conf.urls import url
# -*- encoding: utf-8 -*-
from . import views

urlpatterns = [
    url(r'^$', views.login_view, name='app.login'),
    url(r'^welcome/$', views.welcome_view, name='app.welcome'),
    url(r'^signup/$', views.signup_view, name='app.signup'),
    url(r'^us/$', views.us_view, name='app.us'),
    url(r'^logout/$', views.logout_view, name='app.logout'),
    url(r'^upload/$', views.uploadtrack_view, name='app.uploadtrack'),
    url(r'^music/(?P<slug>[^\.]+)/$', views.track_view, name='app.track'),
    url(r'^member/(?P<slug>[^\.]+)/$', views.userprofile_view, name='app.userprofile'),
    url(r'^update/picture/(?P<slug>[^\.]+)/$', views.updateavatar_view, name='app.updateavatar'),
]