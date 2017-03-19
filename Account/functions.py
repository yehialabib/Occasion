from .models import client,follow
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

def get_followed_clients(user):
    queryset = follow.objects.filter(user=user)
    return queryset


def add_user(password,username,email):
    count1 = User.objects.filter(email=email).count()
    count2 = User.objects.filter(username=username).count()
    if((count1==0)and(count2==0)):
        user = User.objects.create_user(username=username,password=password,email=email)
        print("------------------")
        print("Added new user")
        print(email)
        print(username)
        print("------------------")
        return '{"err":""}'
    else:
        if(count1!=0):
          return '{"err":"Email already exists"}'
        else:
          return '{"err":"Username already exists"}'



# Testing
# get_followed_clients(user = User.objects.all(username='').first())
