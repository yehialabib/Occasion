from Account.models import client
from .models import offer
from django.contrib.auth.models import User
from Account.models import follow
from django.db.models import Sum

def get_total_views(client):
  total = offer.objects.filter(client=client).aggregate(Sum('views'))
  return total

def get_total_clicks(client):
  total = offer.objects.filter(client=client).aggregate(Sum('likes'))
  return total
  
def get_all_offers(client):
    queryset = offer.objects.filter(client=client).order_by('-id')
    return queryset
  
def get_all_user_offers(User):
    Users_follows = follow.objects.filter(user=User)
    displayed_offers = offer.objects.filter(client__in=Users_follows.values('client')).order_by('-timestamp')
    return displayed_offers
  
def add_offer(client, title , photo):
    offer.objects.create(title=title,client=client,photo=photo)
    
def delete(ofer):
    offer.objects.filter(id=ofer).delete()
    
# Testings
#print(get_all_offers(client.objects.filter(name='Fridays').first()))
# print(serializers.serialize("json", get_all_user_offers(User.objects.filter(username="youssef").first())))
#add_offer(client.objects.filter(name='Nike').first(), "New Mercurial Boots","Your dream football shoes are out now!","photo")
#delete(offer.objects.filter(title="1234").first())
