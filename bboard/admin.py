from django.contrib import admin

from .models import Bb, User,Product

# Register your models here.

admin.site.register(Bb)
admin.site.register(User)

admin.site.register(Product)