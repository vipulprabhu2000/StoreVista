
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('payment_sucess',views.payment_sucess,name="payment_sucess"),
    path('Checkout',views.checkout,name="checkout"),
    path('billing_info',views.billing_info, name="billing_info"),
    path('process_order',views.process_order,name="process_order"),
    path('Shipped_order',views.Shipped_order,name="Shipped_order"),
    path('Not_Shipped_order',views.Not_Shipped_order,name="Not_Shipped_order"),
    path('orders/<int:pk>',views.orders,name="orders"),

]
