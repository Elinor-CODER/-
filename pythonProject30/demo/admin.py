from django.contrib import admin

# Register your models here.
from .models import  Product, Order, OrderPosition


class OrderPositionLine(admin.TabularInline):
    model = OrderPosition
    extra = 3

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price']
    list_filter = ['category']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id']
    inlines = [OrderPositionLine]