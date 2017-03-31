from django.shortcuts import render
from Account.models import client,follow
from Account.functions import auth_client
from Offer.functions import get_total_views,get_total_clicks,get_all_offers,add_offer
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
import json
# Create your views here.


def login_view(request):
  if(request.user.pk != None):
      return redirect("home")
  if(request.method == 'POST'):
      username = request.POST.get('username')
      password = request.POST.get('password')
      pk = auth_client(username , password)
      login(request, pk)
      print(pk)
      return redirect("home")
    
  return render(request, "Dashboard/login.html" )  


@login_required
def home(request):
  c = client.objects.filter(user=request.user).first()
  follows = follow.objects.filter(client=c).count()
  total_views = get_total_views(c)
  total_clicks = get_total_clicks(c)
  data = {
    "follows":follows,
    "views":total_views,
    "clicks":total_clicks,
    "client":c,
  }
  return render(request, "Dashboard/index.html" , data )  


@login_required 
def offers(request):
  client1 = client.objects.filter(user=request.user).first()
  offers_all = get_all_offers(client1)
  a=[]
  b=[]
  c=[]
  d=[]
  for i in range(offers_all.count()) :
      if((i+1)%4==0):
        d.append(offers_all[i])
      else:
        if((i+1)%2==0):
           b.append(offers_all[i])
        else:
          if(i+1)%3==0:
             c.append(offers_all[i])
          else :
             a.append(offers_all[i])
  
  offers = {
    "client":client1,
    "first":a,
    "second":b,
    "third":c,
    "fourth":d,
  }
  return render(request, "Dashboard/offers.html",offers)  
  
@login_required  
def system(request):
  return render(request, "Dashboard/system.html")  

@login_required  
def create_offer(request):
  c = client.objects.filter(user=request.user).first()
  data = {
    "client":c,
  }
  if(request.method == 'POST'):
      title = request.POST.get('title')
      image = request.POST.get('image')
      add_offer(c,title,image)
      return redirect("offers")
    
  return render(request, "Dashboard/create_offer.html" ,)  
  
  
  
# print(client.objects.filter(name="Zara").first().id)