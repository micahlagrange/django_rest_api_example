from django.conf.urls import include, url
from django.contrib import admin

import main.views
import main.urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'rest_api_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^users/', include(main.urls), name='users'),

    url(r'^admin/', include(admin.site.urls)),
]
