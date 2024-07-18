from django.shortcuts import render
from cart.cart import Cart
from payment.models import ShippingAddress
from payment.forms import Shippingform

# Create your views here.



def checkout(request):
    cart=Cart(request)
    cart_products=cart.get_prod()
    cart_qty=cart.get_quant()
    total=cart.get_total()
    if request.user.is_authenticated:
        Shipping_user=ShippingAddress.objects.get(user__id=request.user.id)
        shipping_form=Shippingform(request.POST or None, instance=Shipping_user)
        return render(request,"payment/checkout.html",{"cart_product":cart_products,"quantities":cart_qty,"total":total,"shipping_form":shipping_form})
    else:
        shipping_form=Shippingform(request.POST or None)
        return render(request,"payment/checkout.html",{"cart_product":cart_products,"quantities":cart_qty,"total":total,"shipping_form":shipping_form})
    


   
def payment_sucess(request):
    return render(request,"payment/payment_sucess.html",{})