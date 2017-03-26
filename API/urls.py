from django.conf.urls import url,include
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from .account import register,login

urlpatterns = [
  url(r'^register/$',csrf_exempt(register), name='register'),
  url(r'^login/$',csrf_exempt(login), name='login'),
  ]
