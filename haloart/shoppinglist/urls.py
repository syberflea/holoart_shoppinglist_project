from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path(
        'add_cart/<int:product_id>',
        views.add_to_cart,
        name='add_to_cart'
    ),
    path(
        'edit/<int:product_id>',
        views.edit_product,
        name='edit_product'
    ),
    path(
        'delete/<int:product_id>',
        views.delete_product,
        name='delete_product'
    ),
    path(
        'remove/<int:product_id>',
        views.remove_from_cart,
        name='remove_from_cart'
    ),
    path(
        '',
        views.view_cart,
        name='view_cart'
    ),
    path(
        'product_list/',
        views.product_list,
        name='product_list'
    ),
    path(
        'add/',
        views.add_product,
        name='add_product'
    ),
    path(
        'search/',
        views.SearchResultsList.as_view(),
        name='search_results'
    ),
    path(
        'products/',
        views.ProductListView.as_view(),
        name='products'
    )
]
