from ast import mod
from tkinter import CASCADE
import django
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student_db(models.Model):
    student_name = models.ForeignKey(User,on_delete=models.PROTECT)
    student_roll = models.IntegerField()



 