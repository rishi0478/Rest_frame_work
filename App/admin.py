from dataclasses import fields
from django.contrib import admin
from .models import Student_db
# Register your models here.
@admin.register(Student_db)
class Student_reg(admin.ModelAdmin):
    list_display = ['name','age']
