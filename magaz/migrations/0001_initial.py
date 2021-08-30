# Generated by Django 3.2.6 on 2021-08-28 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Название')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Название')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UnderCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Название')),
                ('slug', models.SlugField(unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magaz.category')),
            ],
        ),
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('image', models.ImageField(upload_to='image_product', verbose_name='Изображение')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('slug', models.SlugField(unique=True)),
                ('col_product', models.IntegerField(default=0, verbose_name='Кол. товаров')),
                ('os', models.CharField(choices=[('Android', 'Android'), ('iOS', 'iOS'), ('MUi', 'MUi')], max_length=100, verbose_name='Операционная система')),
                ('cores', models.IntegerField(default=0, verbose_name='Количество ядер')),
                ('ram', models.IntegerField(default=0, verbose_name='Оперативная память')),
                ('memory', models.IntegerField(default=0, verbose_name='Встроенная память')),
                ('bluetooth', models.BooleanField(default=True, verbose_name='Bluetooth')),
                ('wifi', models.BooleanField(default=True, verbose_name='Wi-Fi')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magaz.brand')),
                ('under_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magaz.undercategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('image', models.ImageField(upload_to='image_product', verbose_name='Изображение')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('slug', models.SlugField(unique=True)),
                ('col_product', models.IntegerField(default=0, verbose_name='Кол. товаров')),
                ('cores', models.IntegerField(default=0, verbose_name='Количество ядер')),
                ('ram', models.IntegerField(default=0, verbose_name='Оперативная память')),
                ('os', models.CharField(choices=[('Windows 10 Домашняя', 'Windows 10 Домашняя'), ('Windows 8', 'Windows 8'), ('Windows 7', 'Windows 7'), ('Linux', 'Linux')], max_length=100, verbose_name='Операционная система')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magaz.brand')),
                ('under_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magaz.undercategory')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
