from django.db import models
from django.db.models import UniqueConstraint


class Product(models.Model):
    '''Продукт'''
    name = models.CharField('Наименование', max_length=100)
    description = models.TextField('Описание', null=True)
    image = models.ImageField(
        'Картинка',
        upload_to='media/',
        blank=True
    )
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        constraints = [
            UniqueConstraint(
                fields=('name',),
                name="unique_product",
            )
        ]

    def __str__(self):
        return self.name


class ShopingCart(models.Model):
    '''Список покупок'''
    name = models.CharField('Корзина', max_length=50)
    product = models.ForeignKey(
        Product,
        related_name='shopingcarts',
        on_delete=models.CASCADE,
        verbose_name='список'
    )
    quantity = models.PositiveIntegerField(
        'Количество',
        default=0,
    )

    class Meta:
        verbose_name = 'Список'
        verbose_name_plural = 'Списки'

    def __str__(self):
        return self.name
