from django.contrib import admin

# Register your models here.
from .models import client,follow


admin.site.register(client)
admin.site.register(follow)
