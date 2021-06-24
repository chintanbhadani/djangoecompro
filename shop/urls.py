from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name="shophome"),
    path('about/', views.about,name="AboutUs"),
    path('contact/', views.contact,name="Contact"),
    path('tracker/', views.tracker,name="Tracker"),
    path('search/', views.search,name="Search"),
    path('products/<int:myid>', views.productview,name="Product"),
    path('checkout/', views.checkout,name="Checkout"),
    path('cartpage/', views.cart,name="Checkout"),
    path('sucess/', views.sucess,name="Checkout"),
    
]
