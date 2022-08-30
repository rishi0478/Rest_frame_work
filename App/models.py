from django.db import models

# Create your models here.
class Student_db(models.Model):
    name = models.CharField(max_length=15)
    age = models.CharField(max_length=3)