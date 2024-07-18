from django.shortcuts import render,redirect
from .models import Product,Category,Profile
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm,updateuserform,ChangepasswordForm,UserInfoForm
from django.db.models import Q

from payment.models import ShippingAddress
from payment.forms import Shippingform

import json
from cart.cart import Cart
# Create your views here.

def search(request):

    if request.method=="POST":
        searched_Product=request.POST['Searched']
        #print(searched_Product)
        #searching the obj in the Db
        """ search=Category.objects.filter(name__icontains=searched_Product)
        print(search)
        if search:
            category=Category.objects.get(name=searched_Product)
            Products=Product.objects.filter(category=category)
            return render(request,'search.html',{'searched_Product':Products})
        else:
            messages.success(request,"Product being is Serched is not Present...")
            return render(request,'search.html',{})  """
        search=Product.objects.filter(Q(name__icontains=searched_Product)|Q(description__icontains=searched_Product))
        if not search:
            messages.success(request,"That Product does not exist....")
            return redirect('search')
        else:
            return render(request,'search.html',{'searched_Product':search})
        
    return render(request,'search.html',{})


    

def update_info(request):
    if request.user.is_authenticated:
        current_user=Profile.objects.get(user__id=request.user.id)

        Shipping_user=ShippingAddress.objects.get(user__id=request.user.id)

        shipping_form=Shippingform(request.POST or None, instance=Shipping_user)
        update_user=UserInfoForm(request.POST or None , instance=current_user)

        if update_user.is_valid() or shipping_form.is_valid():
            update_user.save()
            shipping_form.save()
            messages.success(request,"User has Info been Updated !!")
            return redirect('index')
        return render(request,"update_info.html",{"user_form":update_user,"shipping_form":shipping_form})
    else:
        messages.success(request,"You must be Logged in to Access this Page!!")
        return redirect('index')

    

def update_password(request):
    if request.user.is_authenticated:
        current_user=request.user
        if request.method=='POST':
            form=ChangepasswordForm(current_user,request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Password has been changed Successfully!!")
                login(request,current_user)
                return redirect('update_password')
            else:
                for err in list(form.errors.values()):
                    messages.error(request,err)
                    return redirect('update_password')
        else:
            form=ChangepasswordForm(current_user)
            return render(request,"update_password.html",{"form":form})
    else:
        messages.success(request,"You Must be logged in to Access this page......")
        return redirect('login')



def update_user(request):
    if request.user.is_authenticated:
        current_user=User.objects.get(id=request.user.id)
        update_user=updateuserform(request.POST or None , instance=current_user)

        if update_user.is_valid():
            update_user.save()

            login(request,current_user)
            messages.success(request,"User has been Updated !!")
            return redirect('index')
        return render(request,"update_user.html",{"user_form":update_user})
    else:
        messages.success(request,"You must be Logged in to Access this Page!!")
        return redirect('index')
        
def category_summary(request):
    categories=Category.objects.all()
    return render(request,"category_summary.html",{"categories":categories})

def index(request):
    products=Product.objects.all()

    return render(request,"index.html",{'products':products})

def about(request):
    return render(request,"about.html",{})

def login_user(request):

    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user =authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)

            current_user=Profile.objects.get(user__id=request.user.id)
            Dbcart=current_user.Old_cart

            if Dbcart:
                #print(Dbcart)
                cart_data=json.loads(Dbcart)

                cart=Cart(request)
                for key,value in cart_data.items():
                    cart.db_add(product=key,quantity=value)



            messages.success(request,("You have Succcesfully Logged in"))
            return redirect("index")
        else:
            messages.success(request,"Login Unsuccessful")
            return redirect("login")
    else:
        return render(request,"login.html",{})



def logout_user(request):
    logout(request)
    messages.success(request,("You have been logged out Successfully ....... Thank you for Stopping By..."))
    return redirect("index")

def register_user(request):
    form=SignUpForm()
    if request.method=="POST":
        
        form = SignUpForm(request.POST)
        if form.is_valid():
            #print("Success")
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(request, username=username,password=password)
            login(request,user)
            messages.success(request,("You have Registered Sucessfully . Fill out the Profile Info  "))
            return redirect('update_info')
        else:
            messages.success(request,("Oops there was a problem registering .... Please try again"))
            return redirect('register')
    else:
        return render(request,"register.html",{'form':form})


def product(request,pk):
    product=Product.objects.get(id=pk)
    return render(request,'product.html',{'product': product})


def category(request,foo):
    foo=foo.replace('-',' ')
    try:
        category=Category.objects.get(name=foo)
        products=Product.objects.filter(category=category)
        return render(request,"category.html",{'products':products,'category':category})
    except:
        messages.info.success(request,"That Category doesn't Exist!!!!......")
        return redirect('index')
    
