# Generated by Django 4.1.1 on 2022-11-15 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_product_image'),
        ('transaction', '0008_alter_transaction_products_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, through='transaction.TransactionProduct', to='product.product'),
        ),
    ]
