from cgi import print_directory
import queue
from xml.parsers.expat import model
from django.forms import PasswordInput
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.serializer import student_serailizer
from app.models import Student_db
from rest_framework import status
from django.contrib.auth.models import User
from app.serial import student_serail

# Create your views here.

@api_view(['GET', 'POST'])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':

        
        snippets = Student_db.objects.all()
        
        serializer = student_serail(snippets, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        # data = request.POST
        # print(data)
        var = request.data
        num = var['student_name']
        if User.objects.filter(username__exact=num):
            obj = User.objects.filter(username__exact=num).values('id')
            n = obj[0]['id']
            print(n,",,,,,,,,,")
            var['student_name']=n
            print(var)
        else:

            user = User.objects.create_user(username=num)
            user.save()
            obj = User.objects.filter(username__exact=num).values('id')
            n = obj[0]['id']
            var['student_name']=n
            print(var)


        serializer = student_serailizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



