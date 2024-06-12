from django.contrib import admin
from .models import Category,Product,order,Customer


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(order)
admin.site.register(Customer)