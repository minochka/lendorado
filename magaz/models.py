from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from django.contrib.auth.models import User

os_notebook = (
	('Windows 10 Домашняя', 'Windows 10 Домашняя'),
	('Windows 8', 'Windows 8'),
	('Windows 7', 'Windows 7'),
	('Linux', 'Linux')
)

os_smartphone = (
	('Android', 'Android'),
	('iOS', 'iOS'),
	('MUi', 'MUi')
)


class Category(models.Model):
	name = models.CharField(max_length=60, verbose_name='Название')
	slug = models.SlugField(unique=True)

	def __str__(self):
		return self.name


class UnderCategory(models.Model):
	name = models.CharField(max_length=60, verbose_name='Название')
	slug = models.SlugField(unique=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class Brand(models.Model):
	name = models.CharField(max_length=60, verbose_name='Название')
	slug = models.SlugField(unique=True)

	def __str__(self):
		return self.name


class Product(models.Model):
	title = models.CharField(max_length=200, verbose_name='Название')
	image = models.ImageField(upload_to='image_product', verbose_name='Изображение')
	price = models.DecimalField(max_digits=10, decimal_places = 2, verbose_name='Цена')
	slug = models.SlugField(unique=True)
	col_product = models.IntegerField(default=0, verbose_name='Кол. товаров')
	under_category = models.ForeignKey(UnderCategory, on_delete=models.CASCADE)
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

	class Meta:
		abstract = True


class Smartphone(Product):
	os = models.CharField(max_length=100, verbose_name='Операционная система', choices=os_smartphone)
	cores = models.IntegerField(default=0, verbose_name='Количество ядер')
	ram = models.IntegerField(default=0, verbose_name='Оперативная память')
	memory = models.IntegerField(default=0, verbose_name='Встроенная память')
	bluetooth = models.BooleanField(default=True, verbose_name='Bluetooth')
	wifi = models.BooleanField(default=True, verbose_name='Wi-Fi')

	def __str__(self):
		return self.title


class Notebook(Product):
	cores = models.IntegerField(default=0, verbose_name='Количество ядер')
	ram = models.IntegerField(default=0, verbose_name='Оперативная память')
	os = models.CharField(max_length=100, verbose_name='Операционная система', choices=os_notebook)

	def __str__(self):
		return self.title


class CartItem(models.Model):
	user = models.ForeignKey(User, verbose_name='Покупатель', on_delete=models.CASCADE)
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')
	qty = models.PositiveIntegerField(default=1, verbose_name='Количество')
	final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')
	date = models.DateField(auto_now_add=True)


class Cart(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
	products = models.ManyToManyField(CartItem, blank=True)
	total_ptoduct = models.PositiveIntegerField(default=1)
	final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Конечная цена')
	date = models.DateField(auto_now_add=True)

	def __str__(self):
		return "Корзина оформлена: {}, Пользователем: {}".format(str(self.date), str(self.user))