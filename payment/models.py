from django.db import models
from django.contrib.auth.models import User
from store.models import Product
from django.db.models.signals import post_save



class ShippingAddress(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE , null=True, blank=True)
    Shipping_full_name=models.CharField(max_length=500)
    Shipping_email=models.CharField(max_length=500)
    Shipping_address1=models.CharField(max_length=500)
    Shipping_address2=models.CharField(max_length=500)
    Shipping_state=models.CharField(max_length=500,null=True,blank=True)
    Shipping_country=models.CharField(max_length=500)
    Shipping_zipcode=models.CharField(max_length=500)

    class Meta:
        verbose_name_plural="Shipping Address"

    def ___str__(self):
        return f'Shipping Address -{str(self.id)}'
    
def create_Shipping(sender,instance , created ,**kwargs):
    if created:
        user_shipping=ShippingAddress(user=instance)
        user_shipping.save()


post_save.connect(create_Shipping,sender=User)



class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    full_name=models.CharField(max_length=500)
    email=models.CharField(max_length=500)
    Shipping_address=models.TextField(max_length=15000)
    amount_paid=models.DecimalField(max_digits=7,decimal_places=2)
    date_ordered=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order - str(self.id)'


class OrderItem(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    order=models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    quantity=models.PositiveBigIntegerField(default=1)
    price=models.DecimalField(max_digits=7,decimal_places=2) 
    
    def __str__(self):
        return f'Order Item - str(self.id)'

