from .models import Product, ShopingCart
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProductForm

VISIBLE_PAGES = 10


def _get_page_obj(_posts, request):
    paginator = Paginator(_posts, VISIBLE_PAGES)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)


def index(request):
    products = Product.objects.select_related()
    # добавить фильтрацию и сортировку по запросам пользователя
    return render(request, 'shop/index.html', {'products': products})


def add_product(request, product_id):
    '''Обработка данных, введенных пользователем для добавления нового продукта
    сохранение продукта в базу данных.
    '''
    product = Product.objects.get(id=product_id)
    cart_item, created = ShopingCart.objects.get_or_create(product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('shop:view_cart')


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
    return render(request, 'shop/edit_product.html', context)


def delete_product(request, product_id):
    '''Обработка удаления продукта по его идентификатору.'''
    item = ShopingCart.objects.get(id=product_id)
    item.delete()
    return redirect('product_list')


def view_cart(request):
    items = ShopingCart.objects.all()
    total_price = sum(item.product.price * item.quantity for item in items)
    context = {'cart_items': items, 'total_price': total_price}
    return render(
        request,
        'shop/index.html',
        context
    )
