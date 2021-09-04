from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from itertools import chain

from .models import *


def search(request):

	q = request.GET.get('search')

	if q:
		query_sets = []

		products = ProductManager.manager('smartphone', 'notebook')

		products = products.

		words = {
			'products': products,
		}
		return render(request, 'products.html', words)


def home(request):
	category = Category.objects.all()
	products = ProductManager.manager('smartphone', 'notebook')
	words = {
		'category': category,
		'products': products,
	}
	return render(request, 'home.html', words)


def products_category(request, slug):
	categoris =	get_object_or_404(Category, slug=slug)
	under_category = UnderCategory.objects.filter(category=categoris)
	products = ProductManager.manager(slug)
	words = {
		'under_category': under_category,
		'products': products,
	}
	return render(request, 'products_category.html', words)


def products_under_category(request, slug):
	under_category = get_object_or_404(UnderCategory, slug=slug)
	products_notrbooks = Notebook.objects.filter(under_category=under_category)
	products_smartphone = Smartphone.objects.filter(under_category=under_category)
	products = list(chain(products_notrbooks, products_smartphone))
	words = {
		'products': products,
	}
	return render(request, 'products_under_category.html', words)


def product_sale(request):
	products_notrbooks = Notebook.objects.filter(sale=True)
	products_smartphone = Smartphone.objects.filter(sale=True)
	products = list(chain(products_notrbooks, products_smartphone))
	words = {
		'products': products,
	}
	return render(request, 'products.html', words)


def product_all(request):
	products = ProductManager.manager('smartphone', 'notebook')
	words = {
		'products': products,
	}
	return render(request, 'products.html', words)