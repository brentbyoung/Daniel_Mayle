from django.conf.urls import url
from views import index, create
urlpatterns = [
    url(r'^$', index, name='intergration_index'),
    url(r'^usercourse$', create, name='intergration_create'),
]