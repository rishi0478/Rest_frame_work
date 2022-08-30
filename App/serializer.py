from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Student_db

class Student_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student_db
        fields = "__all__"