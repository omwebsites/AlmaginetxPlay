# Create your urls here.
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login_view, name='app.login'),
    url(r'^signup/$', views.signup_view, name='app.signup'),
    url(r'^logout/$', views.logout_view, name='app.logout'),
    url(r'^welcome/$', views.welcome_view, name='app.welcome'),
]