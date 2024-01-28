# Generated by Django 4.2.7 on 2024-01-27 17:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shoppinglist', '0002_alter_product_options_product_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='added_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.AddField(
            model_name='shopingcart',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shopingcart',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Вес (в граммах)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(null=True),
        ),
    ]