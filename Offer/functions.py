from Account.models import client
from .models import offer
from django.contrib.auth.models import User
from Account.models import follow


def get_all_offers(client):
    queryset = offer.objects.filter(client=client)
    return queryset
  
def user_offers_for_display(User):
    Users_follows = follow.objects.filter(user=User)
    displayed_offers = offer.objects.filter(client__in=Users_follows.values('client'))
    return displayed_offers
  
def add_offer(client, title, description, photo):
    offer.objects.create(title=title,client=client,photo=photo,description=description)
    
def delete(ofer):
    offer.objects.filter(id=ofer).delete()
# Testings
#print(get_all_offers(client.objects.filter(name='Fridays').first()))
#user_offers_for_display(User.objects.filter(username="youssef").first())
#add_offer(client.objects.filter(name='Nike').first(), "New Mercurial Boots","Your dream football shoes are out now!","photo")
#delete(offer.objects.filter(title="1234").first())
