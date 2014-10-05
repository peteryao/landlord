from django.conf.urls import patterns, include, url

from . import views

pk = r'(?P<bill_pk>\d+)'

urlpatterns = patterns('core.views',
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    #REGISTRATION
    url(r'^user_registration/$', views.registration_page, name='register'),

    #VENMO
    url(r'^venmo_auth', views.venmo_key, name='venmo_key'),
    url(r'^venmo_payment/{}/$'.format(pk), views.venmo_payment, name='payment'),

    #MOXTRA
    url(r'moxtra_update/', views.moxtra_todo_api, name='moxtra_todo'),
)