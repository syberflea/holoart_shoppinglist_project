import django_filters

from .models import Product, ShopingCart


class ProductFilter(django_filters.FilterSet):

    class Meta:
        model = Product
        fields = ['name', 'price']


class ShopingCartFilter(django_filters.FilterSet):
    class Meta:
        model = ShopingCart
        fields = ('product', 'quantity')
