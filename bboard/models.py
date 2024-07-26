from django.db import models

# Create your models here.


class Bb(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    content = models.TextField()



class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()

