from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('products/<str:slug>/', products_category, name='products_category'),
    path('product/<str:slug>/', products_under_category, name='products_under_category'),
    path('products/sale', product_sale, name='products_sale'),
    path('products/', product_all, name='products_all'),
    path('search/', search, name='search')
]