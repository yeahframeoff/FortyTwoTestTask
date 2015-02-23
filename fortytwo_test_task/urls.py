from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'main.views.mainpage', name='main'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^requests/', 'requests_saver.views.requestspage', name='requests'),
)
