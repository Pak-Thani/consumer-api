# Generated by Django 4.1.1 on 2022-11-11 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_product_image'),
        ('transaction', '0004_alter_transaction_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='product',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='total',
            field=models.PositiveIntegerField(),
        ),
        migrations.CreateModel(
            name='TransactionProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('transaction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='transaction.transaction')),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='products',
            field=models.ManyToManyField(through='transaction.TransactionProduct', to='product.product'),
        ),
    ]