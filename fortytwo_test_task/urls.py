from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from main import views as mainviews

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', mainviews.mainpage, name='main'),
    url(r'^admin/', include(admin.site.urls)),
)
