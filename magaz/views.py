from django.shortcuts import render

from .models import Cart


def home(request):
	carts = Cart.objects.all()
	return render(request, 'home.html', {'carts': carts})


def new_list(request):
	return render(request, 'new_list.html')