from django.shortcuts import render,get_object_or_404
from .cart import Cart
from store.models import Product 
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.


def cart_summary(request):
    cart=Cart(request)
    cart_products=cart.get_prod()
    cart_qty=cart.get_quant()
    total=cart.get_total()
    return render(request,"cart_summary.html",{"cart_product":cart_products,"quantities":cart_qty,"total":total})

def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action')=="post":
        product_id=int(request.POST.get('product_id'))
        product_qty=int(request.POST.get('product_qty'))
        product=get_object_or_404(Product,id=product_id)
        cart.add(product=product,quantity=product_qty)
        cart_quantity=cart.__len__()
        #response=JsonResponse({'Product Name : ': product.name})
        response=JsonResponse({'qty': cart_quantity})
        messages.success(request,"The Product Successfully added to your Cart ......")
        return response


def cart_delete(request):
    cart= Cart(request)

    if request.POST.get('action')=='post':
        Product_id=request.POST.get('product_id')

        cart.delete_item(Product_id)
        response=JsonResponse({'product_id':Product_id})
        messages.success(request,"Item was deleted from your Cart ......")
        return response


def cart_update(request):
    cart =Cart(request)
    if request.POST.get('action')=='post':

        Product_id=request.POST.get('product_id')
        Product_qty=request.POST.get('product_qty')
        print(f"Quantity{Product_qty}")

        cart.update(product=Product_id,Quantity=Product_qty)

        response=JsonResponse({'qty':Product_qty})
        messages.success(request,"The Cart was Updated.....")
        return response

