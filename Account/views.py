from django.shortcuts import render
import json
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Account.functions import get_followed_clients
from Account.models import client,follow


def account(request):
     user = request.user
     if(client.objects.filter(user=user).count()==0):
         follows = get_followed_clients(user)
         data = {
         'follows':follows,
         'user':user
         }
         return render(request, "Account/account.html",data)
     else:
         c=client.objects.filter(user=user).first()
         data={
            'client':c,
            'followers': str(follow.objects.filter(client=c).count())
         }
         return render(request, "Account/dashboard.html",data)
