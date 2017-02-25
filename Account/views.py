from django.shortcuts import render
import json
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Account.functions import get_followed_clients,add_user
from Account.models import client,follow
from Offer.functions import get_all_offers
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate


# def account(request):
#      user = request.user
#      if(client.objects.filter(user=user).count()==0):
#          follows = get_followed_clients(user)
#          data = {
#          'follows':follows,
#          'user':user
#          }
#          return render(request, "User/account.html",data)
#      else:
#          c=client.objects.filter(user=user).first()
#          offers = get_all_offers(c)
#          data={
#             'client':c,
#             'followers': str(follow.objects.filter(client=c).count()),
#             'offers': offers
#          }
#          return render(request, "Client/dashboard.html",data)

def auth(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if(user!='None'):
             login(request,user)
             return HttpResponseRedirect("/account/")

def account(request):
    if request.user.is_authenticated():
        user = request.user
        if(client.objects.filter(user=user).count()==0):
            follows = get_followed_clients(user)
            data = {
            'follows':follows,
            'user':user
            }
            return render(request, "User/account.html",data)
        else:
            c=client.objects.filter(user=user).first()
            offers = get_all_offers(c)
            data={
               'client':c,
               'followers': str(follow.objects.filter(client=c).count()),
               'offers': offers
            }
            return render(request, "Client/dashboard.html",data)
    else:
        return render(request, "Landing/login.html")


def signUp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        pass_1 = request.POST.get('password1')
        pass_2 = request.POST.get('password2')
        if pass_1 == pass_2:
            add_user(first_name,last_name,pass_1,username,email)

        else:
             error = " Password Mismatch "
