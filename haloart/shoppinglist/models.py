from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    '''Продукт'''
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.PositiveIntegerField(
        'Количество (в граммах)',
        default=1,
        validators=[
            MinValueValidator(
                1,
                message='Минимальное количество 1 гр'
            ),
        ]
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ShopingCart(models.Model):
    '''Список покупок'''
    product = models.ForeignKey(
        Product,
        related_name="shopingcarts",
        on_delete=models.CASCADE,
        verbose_name='список'
    )

    class Meta:
        verbose_name = 'Список'
        verbose_name_plural = 'Списки'
