from django.shortcuts import render
from cart.cart import Cart
from payment.models import ShippingAddress,Order,OrderItem
from payment.forms import Shippingform,Payment_form
import django.contrib.messages as messages 
from django.contrib.auth.models import User

# Create your views here.
def process_order(request):
    if request.POST:

        cart=Cart(request)
        cart_product=cart.get_prod()
        cart_qty=cart.get_quant()
        total=cart.get_total()
    
        payment_form=Payment_form(request.POST or None)
        my_shipping=request.session.get('my_shipping')
        shipping_Address=f"{my_shipping['Shipping_address1']}\n{my_shipping['Shipping_address2']}\n{my_shipping['Shipping_state']}\n{my_shipping['Shipping_country']}\n{my_shipping['Shipping_zipcode']}\n"
        print(shipping_Address)
        full_name=my_shipping['Shipping_full_name']
        email=my_shipping['Shipping_email']
        amount_paid=my_shipping['totals']

        if request.user.authenticated:
            user=request.user
            create_order=Order(user=user,full_name=full_name,email=email,amount_paid=amount_paid,Shipping_address=shipping_Address)
            create_order.save()
            messages.success(request,"Order Placed!!")
            return render(request,'index.html',{})

        else:
            create_order=Order(full_name=full_name,email=email,amount_paid=amount_paid,Shipping_address=shipping_Address)
            create_order.save()
            messages.success(request,"Order Placed!!")
            return render(request,'index.html',{})



    else:
        messages.success(request,"Access Denied!!")
        return render(request,'index.html',{})

def billing_info(request):
    if request.POST:
        cart=Cart(request)
        cart_product=cart.get_prod()
        cart_qty=cart.get_quant()
        total=cart.get_total()

        my_shipping=request.POST
        request.session['my_shipping']=my_shipping

        if request.user.is_authenticated:
            billing_form=Payment_form()
            return render(request,"payment/billing_info.html",{"cart_product":cart_product,"quantities":cart_qty,"total":total,"shipping_info":request.POST,"billing_form":billing_form})
        else:
            billing_form=Payment_form()
            messages.success(request,"AccessDenied")
            return render(request,"index.html",{})
        

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