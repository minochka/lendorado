from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('new_list/', new_list, name='new_list')
]