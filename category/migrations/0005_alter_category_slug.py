# Generated by Django 4.1.1 on 2022-12-08 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_remove_category_icon_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(editable=False, max_length=100, unique=True),
        ),
    ]