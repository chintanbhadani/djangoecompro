from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


# static(settings.MEDIA_URL, do cument_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   

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
