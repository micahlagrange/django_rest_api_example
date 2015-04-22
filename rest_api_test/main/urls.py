from django.conf.urls import url

import main.views

urlpatterns = [
    url(r'^$', main.views.make_user, name='make_user'),
    url(r'^(?P<user_id>\d+)/$', main.views.user_by_id, name='user_by_id'),
]
