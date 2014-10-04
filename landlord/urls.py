from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'esports_management.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('core.urls')),
    url(r'^admin/', include(admin.site.urls)),
)