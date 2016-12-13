from django.conf.urls import url
from views import users, users_w_id, new, edit, destroy

# Remember, the 'products' portion of the url was devoured by the main urls.py file
urlpatterns = [
    # This route deals w/ GET and POST to users (either index or create)
    url(r'^$', users),
    url(r'^new$', new),
    # This route deals w/ GET and POST to /users/<id> (either update or show)
    url(r'^(?P<id>\d+)/$', users_w_id),
    url(r'^(?P<id>\d+)/edit/$', edit),
    url(r'^(?P<id>\d+)/destroy/$', destroy),
]