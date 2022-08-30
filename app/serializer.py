
from pyexpat import model
from rest_framework import serializers
from app.models import Market_Product,Buyer
class product_serializer(serializers.ModelSerializer):
    class Meta:
        model = Market_Product
        fields = ['product_name','product_ID','name']
        # depth = 1


class buyer_serializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ['name','buyer_name']
        # depth = 1

