from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create), #creats a localhost 8000/create
    url(r'^reset$', views.reset) #creats a localhost 8000/reset
] 