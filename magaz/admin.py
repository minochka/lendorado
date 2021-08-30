from django.contrib import admin

from .models import *

admin.site.register(Smartphone)
admin.site.register(Notebook)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(UnderCategory)
admin.site.register(Brand)
admin.site.register(CartItem)