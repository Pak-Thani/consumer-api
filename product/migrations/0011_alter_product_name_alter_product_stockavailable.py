# Generated by Django 4.1.1 on 2023-01-04 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='product',
            name='stockAvailable',
            field=models.PositiveIntegerField(default=0),
        ),
    ]