from pyexpat import model
from urllib import request
from django.db import models
from django.core import validators
from django.core.validators import RegexValidator
# Create your models here.

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$','only alpha numeric characters are allowed')

class Market_Product(models.Model):
    name = models.CharField(max_length=12, null= True)
    product_name = models.CharField(max_length=12, null=True)
    product_ID = models.CharField(validators=[validators.MaxLengthValidator(8),alphanumeric],unique=True,max_length=10,null=True)


class Buyer(models.Model):
    buyer_name = models.ManyToManyField(Market_Product)
    name = models.CharField(max_length=12, null=True)
    