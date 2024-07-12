from django.db import models
from django.contrib.auth.models import User


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

