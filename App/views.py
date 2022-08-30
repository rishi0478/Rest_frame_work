from importlib.resources import Resource
from operator import is_
from xmlrpc.client import ResponseError
from django.shortcuts import render
from rest_framework.response import Response
from App.models import Student_db
from App.serializer import Student_serializer
from rest_framework import status
from rest_framework import viewsets

# Create your views here.

class Stu_Operation(viewsets.ViewSet):
    def list(self,request):
        obj = Student_db.objects.all()
        serializer = Student_serializer(obj,many=True)
        try:
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk):
        try:
            obj_instance = Student_db.objects.get(pk=pk)
        except Exception as e:
            return Response("id not exsist")
        serializer = Student_serializer(obj_instance)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

    def create(self,request):
        try:
            serializer = Student_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk):
        try:
            obj_instace = Student_db.objects.get(pk=pk)
        except Exception as e:
            return Response("Data is not store Because this id Does not Exsist")

        serializer = Student_serializer(obj_instace,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_502_BAD_GATEWAY)
    
    def partial_update(self,request,pk):
        obj_instance = Student_db.objects.get(pk=pk)
        serializer = Student_serializer(obj_instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Parital data Updated"})
        return Response(serializer.errors)

    def destroy(sekf,request,pk):
        obj_instance = Student_db.objects.get(pk = pk)
        obj_instance.delete()
        return Response("Data is deleted!")
        
        
            

        
            
    




