from django.conf.urls import url
from views import index, create, destroy

urlpatterns = [
    url(r'^$', index),
    url(r'^create$', create),
    url(r'^(?P<id>\d+)/destroy$', destroy),
]