
from rest_framework import serializers
from django.contrib.auth.models import User
from app.models import Student_db
class user_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
        # depth = 1

class student_serail(serializers.ModelSerializer):
    # student_name=serializers.StringRelatedField()
    student_name = serializers.StringRelatedField( read_only=True)

    class Meta:
        model = Student_db
        fields = ["student_name","student_roll"]