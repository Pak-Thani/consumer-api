# Generated by Django 4.1.1 on 2022-09-13 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=150)),
                ('image', models.CharField(max_length=150)),
                ('slug', models.CharField(max_length=30)),
            ],
        ),
    ]