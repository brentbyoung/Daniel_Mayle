from django.conf.urls import url
# from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^emails$', views.create),
    url(r'^success$', views.success),
    url(r'^emails/(?P<id>[0-9]*)/delete', views.destroy)
]