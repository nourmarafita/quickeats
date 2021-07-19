from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Pizza(models.Model):
    name   = models.CharField(max_length=120)
    priceM = models.IntegerField(blank=True, null=True)
    priceL = models.IntegerField(blank=True, null=True)
    pImage = models.URLField()


class Burger(models.Model):
    name   = models.CharField(max_length=120)
    priceM = models.IntegerField(blank=True, null=True)
    priceL = models.IntegerField(blank=True, null=True)
    bImage = models.URLField()

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    number   = models.CharField(max_length=60)
    bill     = models.IntegerField(blank=True, null=True)
    date     = models.DateTimeField(default=now, editable=False)
    note     = models.TextField(blank=True, null=True)

class Item(models.Model):
    order  = models.ForeignKey(Order, on_delete=models.CASCADE)
    name   = models.CharField(max_length=120)
    price  = models.IntegerField(blank=True, null=True)
    size   = models.CharField(max_length=60)
