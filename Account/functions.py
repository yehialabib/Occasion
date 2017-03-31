from .models import client,follow
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.core import serializers

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
          return '{"err" : "Email already exists"}'
        else:
          return '{"err" : "Username already exists"}'
        
def auth( username , password ):
  user = authenticate( username=username, password=password )
  if(user != None):
     return '{"err" : "" , "pk" : ' + str(user.id) + '}'
    
  else:
      return '{"err":"Username Or Password Incorrect"}'
    
    
def auth_client( username , password ):
  user = authenticate( username=username, password=password )
  if(user != None):
     check = client.objects.filter(user=user.id)
     if(check.count()>0):
        return user
     else:
      return 'none'
  else:
      return 'none'



# Testing
# get_followed_clients(user = User.objects.all(username='').first())
# print(auth('youssef','hesoyamhesoyam'))
# x = serializers.serialize("json", follow.objects.filter(user = 1))
# print(x)
# print(auth_client('zara','hesoyamhesoyam'))