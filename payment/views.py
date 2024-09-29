from django.shortcuts import render,redirect
from cart.cart import Cart
from payment.models import ShippingAddress,Order,OrderItem
from payment.forms import Shippingform,Payment_form
import django.contrib.messages as messages 
from django.contrib.auth.models import User
from datetime import datetime
import datetime
from store.models import Profile

def orders(request,pk):
    if request.user.is_authenticated and request.user.is_superuser:
        order=Order.objects.get(id=pk)
        items=OrderItem.objects.filter(order=pk)

        if request.POST:
            status=request.POST['shipped_status']
            order=Order.objects.filter(id=pk)
            now=datetime.datetime.now()

            if status=="True":
                order.update(shipped=True,date_shipped=now)

            else:
                order.update(shipped=False,date_shipped=now)
            messages.success(request,"Updated")
            return redirect('index')
            

        return render(request,"payment/orders.html",{"order":order,"items":items})
    else:
        messages.success(request,"Access Denied!!")
        return redirect('index')

def Not_Shipped_order(request):
    if request.user.is_authenticated and request.user.is_superuser:
        orders=Order.objects.filter(shipped=False)
        return render(request,"payment/Not_Shipped_order.html",{"orders":orders})
    else:
        messages.success(request,"Access Denied!!")
        return redirect('index.html')


def Shipped_order(request):
    if request.user.is_authenticated and request.user.is_superuser:
        orders=Order.objects.filter(shipped=True)
        return render(request,"payment/Shipped_order.html",{"orders":orders})
    else:
        messages.success(request,"Access Denied!!")
        return render(request,'index.html',{})




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
        amount_paid=total

        def common_orderitem_creation(create_order,flag):
                order_id=create_order.pk
                user=request.user
                for products in cart_product:
                    product_id=products.id
                    if products.is_sale:
                        price=products.sale_price
                    else:
                        price=products.price

                    for key,value in cart_qty.items():
                        if int(key)==product_id:
                            if(flag==1):
                                create_order_item=OrderItem(user=user,order_id=order_id,product_id=product_id,quantity=value,price=price)
                            else:
                                create_order_item=OrderItem(order_id=order_id,product_id=product_id,quantity=value,price=price)
                            create_order_item.save()

                for key in list(request.session.keys()):
                    if key=="session_key":
                        #dictionary with Product id and quantity
                        print(request.session[key])
                        del request.session[key]
                
                current_user=Profile.objects.filter(user__id=request.user.id)
                current_user.update(Old_cart="")

                messages.success(request,"Order Placed!!")

        if request.user.is_authenticated:
            user=request.user
            create_order=Order(user=user,full_name=full_name,email=email,amount_paid=amount_paid,Shipping_address=shipping_Address)
            create_order.save()
            

            common_orderitem_creation(create_order,flag=1)
            return render(request,'index.html',{})


        else:
            create_order=Order(full_name=full_name,email=email,amount_paid=amount_paid,Shipping_address=shipping_Address)
            create_order.save()
            common_orderitem_creation(create_order,flag=2)
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
            return render(request,"payment/billing_info.html",{"cart_product":cart_product,"quantities":cart_qty,"total":total,"shipping_info":request.POST,"billing_form":billing_form})
        
       


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