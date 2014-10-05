from django.conf.urls import patterns, include, url

from . import views

pk = r'(?P<unit_pk>\d+)'
user_pk = r'(?P<user_pk>\d+)'

urlpatterns = patterns('',
    url(r'^unit/{}/$'.format(pk), views.unit_index, name='single_unit'),
    url(r'^unit/{}/set_rent/$'.format(pk), views.set_rent, name='managment_set_rent'),
    url(r'^unit/{}/update_rent/$'.format(pk), views.update_rent, name='management_update_rent'
        ),
 )