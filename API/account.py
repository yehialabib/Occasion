from Account.functions import add_user,auth
from django.http import HttpResponse


def register(request):
    if request.method == 'GET':
        email = request.GET.get('email')
        username = request.GET.get('username')
        password = request.GET.get('password')
        add = add_user(password,username,email)
        return HttpResponse(add)
      
def login(request):
   if request.method == 'GET':
        username = request.GET.get('username')
        password = request.GET.get('password')
        login = auth(username,password)
        return HttpResponse(login)
      
