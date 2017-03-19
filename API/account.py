from Account.functions import add_user
from django.http import HttpResponse


def register(request):
    if request.method == 'GET':
        email = request.GET.get('email')
        username = request.GET.get('username')
        password = request.GET.get('password')
        add = add_user(password,username,email)
        return HttpResponse(add)
