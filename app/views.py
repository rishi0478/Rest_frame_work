from curses import reset_prog_mode
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from app.models import Market_Product,Buyer
from app.serializer import product_serializer, buyer_serializer
# Create your views here.
@api_view(['GET','POST'])
def func(request):
    if request.method == 'GET':
        raw_data = Market_Product.objects.all()
        serializer = product_serializer(raw_data,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        dol = request.data
        print(dol,"---------------------")



        
        # if Buyer.objects.filter(name__exact = dol['name'])
        serializer = product_serializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            var = Buyer.objects.create(name = dol['name'])
            nn = Market_Product.objects.filter(product_name__exact= dol['product_name']).first()
            var.buyer_name.add(nn)
            return Response(serializer.data , status= status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def func2(request,id):

    try:
        key = Buyer.objects.get(id = id)
    except Buyer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        raw_data = Buyer.objects.all()
        serializer = buyer_serializer(raw_data,many=True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        
        serializer = buyer_serializer(key,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







