from .models import client,follow
from django.contrib.auth.models import User

def get_followed_clients(user):
    queryset = follow.objects.filter(user=user)
    return queryset


# Testing
# get_followed_clients(user = User.objects.all(username='').first())
