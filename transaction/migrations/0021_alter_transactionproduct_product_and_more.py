# Generated by Django 4.1.1 on 2022-11-16 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_product_image'),
        ('transaction', '0020_alter_transactionproduct_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AlterField(
            model_name='transactionproduct',
            name='transaction',
            field=models.ForeignKey(blank=True, default=5, null=True, on_delete=django.db.models.deletion.CASCADE, to='transaction.transaction'),
        ),
    ]