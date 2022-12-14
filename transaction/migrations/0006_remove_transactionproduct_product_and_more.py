# Generated by Django 4.1.1 on 2022-11-14 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_product_image'),
        ('transaction', '0005_remove_transaction_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactionproduct',
            name='product',
        ),
        migrations.AddField(
            model_name='transactionproduct',
            name='productID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
            preserve_default=False,
        ),
    ]
