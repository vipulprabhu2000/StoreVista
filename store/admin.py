from django.contrib import admin
from .models import Category,Product,order,Customer,Profile
from django.contrib.auth.models import User


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(order)
admin.site.register(Customer)
admin.site.register(Profile)

class ProfileInline(admin.StackedInline):
    model=Profile

class UserAdmin(admin.ModelAdmin):
    model=User
    field=["username","First_name","Last_name","Email"]
    inlines=[ProfileInline]


admin.site.unregister(User)

admin.site.register(User,UserAdmin)