"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from apps.cart.views import cart_detail
from apps.core.views import frontpage,contact,about
from apps.store.views import product_detail, category_detail

from apps.store.api import api_add_to_cart,api_remove_from_cart

urlpatterns = [
    path('',frontpage, name='frontpage'),
    path("cart/", cart_detail, name="cart"),
    path('contact/',contact, name='contact'),
    path('about/',about, name='about'),
    path('admin/', admin.site.urls),
    #API
    
    path("api/add_to_cart/", api_add_to_cart, name="api_add_to_cart"),
    path("api/remove_from_cart/", api_remove_from_cart, name="remove_from_cart"),
    #Store
    path('<slug:category_slug>/<slug:slug>/',product_detail, name='product_detail'),
    path('<slug:slug>/',category_detail, name='category_detail'),
    

]
