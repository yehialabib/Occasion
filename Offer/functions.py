from Account.models import client
from .models import offer


def get_all_offers(client):
    queryset = offer.objects.filter(client=client)
    return queryset

# Testing
print(get_all_offers(client.objects.filter(name='Fridays').first()))
