from .functions import get_followed_clients
from django.conf.urls import url,include
from django.contrib import admin
from .views import account

app_name = 'Account'
urlpatterns = [
  url(r'^$',account, name='account'),
  ]
  # url(r'^get_video/$', get_video , name='get_video'),
