from django.conf.urls import url
from views import index, login, register, success, logout
urlpatterns = [
    url(r'^$', index, name='users_index'),
    url(r'^login$', login, name='users_login'),
    url(r'^register$', register, name='users_register'),
    url(r'^success$', success, name='users_success'),
    url(r'^logout$', logout, name='users_logout'),
]