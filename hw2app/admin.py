from django.contrib import admin
from django.db import models
from .models import ProductModel, ClientModel, OrderModel
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
    ordering = ['price']
    search_fields = ['name']
    search_help_text = 'Поиск по названию продукта (NAME)'

class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']
    search_fields = ['name']
    search_help_text = 'Поиск по названию продукта (NAME)'

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'get_products_list', 'total_price']
    list_filter = ['date_order', 'total_price']


admin.site.register(ClientModel, ClientAdmin)
admin.site.register(ProductModel,ProductAdmin)
admin.site.register(OrderModel, OrderAdmin)