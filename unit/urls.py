from django.conf.urls import patterns, include, url

from . import views

pk = r'(?P<todo_pk>\d+)'
bill_pk = r'(?P<bill_pk>\d+)'

urlpatterns = patterns('',
    url(r'^add_task/$', views.add_task, name='add_task'),
    url(r'^finish_todo/{}/$'.format(pk), views.finish_todo, name='finish_todo'),
    url(r'^bill_payment/{}/$'.format(bill_pk), views.venmo_bill_payment, name='bill_payment'),
 )