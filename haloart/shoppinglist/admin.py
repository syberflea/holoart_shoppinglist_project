from django.contrib import admin
from .models import ShopingCart, Product


@admin.register(ShopingCart)
class ShopingCartAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
