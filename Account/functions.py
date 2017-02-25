from .models import client,follow
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

def get_followed_clients(user):
    queryset = follow.objects.filter(user=user)
    return queryset
def addUser(first_name,last_name,password,username,email):
	count=User.objects.filter(email=email).count()
	if count==0:
	 	user = User.objects.create_user(
                                              username=username,
                                              password=password,
                                              first_name=first_name,
                                              last_name=last_name,
                                              email=email,
                                            )
		newUser = authenticate(username=User.username, password=password)
		return True
	else:
		return False



# Testing
# get_followed_clients(user = User.objects.all(username='').first())
