from .models import Product, ShopingCart
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProductForm

VISIBLE_PAGES = 10


def _get_page_obj(_posts, request):
    paginator = Paginator(_posts, VISIBLE_PAGES)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)


def product_list(request):
    products = Product.objects.select_related()
    # добавить фильтрацию и сортировку по запросам пользователя
    return render(request, 'shop/product_list.html', {'products': products})


def add_product(request):
    '''Обработка данных, введенных пользователем для добавления нового продукта
    сохранение продукта в базу данных.
    '''
    form = ProductForm(
        request.POST or None,
        files=request.FILES or None)
    if form.is_valid():
        item = form.save(commit=False)
        item.save()
        print(item)
        return redirect('shop:product_list')
    context = {
        'form': form,
        'is_edit': False
    }
    return render(request, 'shop/create_product.html', context)


def edit_product(request, product_id):
    '''
    Обработка редактирования продукта по его идентификатору.
    отображение формы для редактирования продукта.
    '''
    product = get_object_or_404(Product, pk=product_id)
    form = ProductForm(
        request.POST or None,
        files=request.FILES or None,
        instance=product
    )
    if form.is_valid():
        form.save()
        return redirect('shop:edit_product', product_id)
    context = {
        'product': product,
        'form': form,
        'is_edit': True
    }
    return render(request, 'shop/create_product.html', context)


def delete_product(request, product_id):
    '''Обработка удаления продукта по его идентификатору.'''
    item = get_object_or_404(Product, pk=product_id)
    item.delete()
    return redirect('shop:product_list')


def view_cart(request):
    items = ShopingCart.objects.all()
    total_price = sum(item.product.price * item.quantity for item in items)
    context = {'cart_items': items, 'total_price': total_price}
    return render(
        request,
        'shop/index.html',
        context
    )


def add_to_cart(reuest, product_id):
    '''Добавление выбранного продукта в корзину.'''
    product = Product.objects.get(id=product_id)
    cart_item, created = ShopingCart.objects.get_or_create(product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('shop:view_cart')


def remove_from_cart(request, product_id):
    '''Удаление выбранного продукта из корзины.'''
    item = ShopingCart.objects.get(id=product_id)
    item.delete()
    return redirect('shop:view_cart')
