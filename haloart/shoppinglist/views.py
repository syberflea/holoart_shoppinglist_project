from .models import Product
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

VISIBLE_POSTS = 10


def _get_page_obj(_posts, request):
    paginator = Paginator(_posts, VISIBLE_POSTS)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)


def index(request):
    products = Product.objects.all()
    # добавить фильтрацию и сортировку по запросам пользователя
    return render(request, 'shop/index.html', {'products': products})


def product_list(request):
    products = Product.objects.all()
    # здесь можно добавить фильтрацию и сортировку по запросам пользователя
    return render(request, 'product_list.html', {'products': products})


def add_product(request):
    if request.method == 'POST':
        # обработка данных, введенных пользователем для добавления нового продукта
        # сохранение продукта в базу данных
        return redirect('product_list')
    else:
        # отображение формы для добавления продукта
        return render(request, 'add_product.html')


def edit_product(request, product_id):
    # обработка редактирования продукта по его идентификатору
    # отображение формы для редактирования продукта
    return render(request, 'edit_product.html', {'product': product})


def delete_product(request, product_id):
    # обработка удаления продукта по его идентификатору
    return redirect('product_list')
