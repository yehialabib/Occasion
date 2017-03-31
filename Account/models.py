from django.db import models
from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

# Create your models here.
class client(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    logo = models.CharField(max_length=500)
    name = models.CharField(max_length=20)
    phone_num = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    description = models.TextField( null=True)
    def __str__(self):
        return self.name

class follow(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    client = models.ForeignKey(client,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username + " - " + self.client.name
