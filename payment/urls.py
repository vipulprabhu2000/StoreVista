
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('payment_sucess',views.payment_sucess,name="payment_sucess"),
    path('Checkout',views.checkout,name="checkout")

]
