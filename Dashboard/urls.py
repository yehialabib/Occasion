from django.conf.urls import url,include
from django.contrib import admin
from .views import home,offers,system,login_view,create_offer

urlpatterns = [
  url(r'^home/$',home, name='home'),
  url(r'^offers/$',offers, name='offers'),
  url(r'^system/$',system, name='system'),
  url(r'^$',login_view, name='login'),
  url(r'^createOffer$',create_offer, name='create offer'),
  ]
  # url(r'^get_video/$', get_video , name='get_video'),
