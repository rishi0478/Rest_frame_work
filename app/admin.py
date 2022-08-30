from django.contrib import admin
from app.models import Market_Product,Buyer
# Register your models here.

@admin.register(Market_Product)
class product_admin(admin.ModelAdmin):
    list_display = ['product_name','product_ID']

admin.site.register(Buyer)

