from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('core.views',
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),

    #VENMO
    url(r'^venmo_auth', views.venmo_key, name='venmo_key')
)