from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from main.views import mainpage
from requests_saver.views import requestspage

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', mainpage),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^requests/', requestspage, name='requests'),
)
