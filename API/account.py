from Account.functions import add_user
from django.http import HttpResponse


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        if(add_user(first_name,last_name,password,username,email)==True):
             return HttpResponse("")
        else:
             return HttpResponse("Email already exists")
