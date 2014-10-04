from django.conf.urls import patterns, include, url

from . import views

pk = r'(?P<unit_pk>\d+)'
user_pk = r'(?P<user_pk>\d+)'

urlpatterns = patterns('esport',
    url(r'^unit/{}/$'.format(pk), views.unit_index, name='single_unit'),
 )