from django.db import models
from django.contrib.auth.models import User
from Account.models import client


class offer(models.Model):
    client = models.ForeignKey(client,on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    photo = models.CharField(null=True, max_length=200)
    branch = models.CharField(null=True, max_length=1000)
    description = models.TextField(null=True, max_length=1000)
    timestap = models.DateTimeField(auto_now=False, auto_now_add=True)
    no_of_likes = models.IntegerField()
    views = models.IntegerField()
    def __str__(self):
        return self.client.name
