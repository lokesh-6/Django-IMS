from django.contrib import admin
from .models import Product,Order
from django.contrib.auth.models import Group

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','category','quantity')

class OredrsAdmin(admin.ModelAdmin):
    list_display=('product','staff','order_quantity','date')

admin.site.site_header='IMS Dashboard'
admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OredrsAdmin)


 