from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'main.views.mainpage', name='main'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^requests/', 'requests_saver.views.requestspage', name='requests'),
    url(r'^userdata/', 'main.views.editpage', name='edit'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
