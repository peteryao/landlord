from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('core.views',
    #MOXTRA
    #PAYPAL
    url(r'^test/', views.view_that_asks_for_money, name="test"),
)