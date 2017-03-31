from django.conf.urls import url,include
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from .account import register,login
from .offer import offers_home 

urlpatterns = [
  url(r'^register/$',csrf_exempt(register), name='register'),
  url(r'^login/$',csrf_exempt(login), name='login'),
  url(r'^offers_home/$',csrf_exempt(offers_home), name='offers_home'),
  ]
