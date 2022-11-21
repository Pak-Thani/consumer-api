# Generated by Django 4.1 on 2022-11-21 11:23

from django.db import migrations
import image_optimizer.fields


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_alter_category_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='icon',
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=image_optimizer.fields.OptimizedImageField(default=1, upload_to='icon-category/'),
            preserve_default=False,
        ),
    ]
