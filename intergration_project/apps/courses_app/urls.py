from django.conf.urls import url
from views import index, create, destroy

urlpatterns = [
    url(r'^$', index, name='courses_index'),
    url(r'^create$', create, name='courses_create'),
    url(r'^(?P<id>\d+)/destroy$', destroy, name='courses_destroy'),
]