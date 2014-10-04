from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('core.views',
    #MOXTRA
    # url(r'^moxtra/redirect_check/$'),
    url(r'^mtest/$', views.mtest, name="chat"),
    #PAYPAL
    url(r'^test/$', views.view_that_asks_for_money, name="test"),
)