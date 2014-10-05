from django.conf.urls import patterns, include, url

from . import views

pk = r'(?P<unit_pk>\d+)'
user_pk = r'(?P<user_pk>\d+)'

urlpatterns = patterns('',
    url(r'^add_task/$', views.add_task, name='add_task'),
 )