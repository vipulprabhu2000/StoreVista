from django.db import models
import datetime


class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Customer(models.Model):
    First_name=models.CharField(max_length=50)
    Last_name=models.CharField(max_length=50)
    Phone=models.CharField(max_length=10)
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.First_name}{self.Last_name}'

class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.DecimalField(default=0,decimal_places=2,max_digits=6)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description=models.CharField(max_length=250,default='',blank=True,null=True)
    image=models.ImageField(upload_to='uploads/product/')
    
    is_sale=models.BooleanField(default=False)
    sale_price=models.DecimalField(default=0,max_digits=6,decimal_places=2)
    
    def __str__(self):
        return self.name
    


class order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    address=models.CharField(max_length=250,default='',blank=True)
    phone=models.CharField(max_length=20,default='',blank=True)
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.product


