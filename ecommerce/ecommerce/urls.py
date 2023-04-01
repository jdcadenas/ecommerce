from django.contrib import admin

from django.conf import settings  # new
from django.urls import path, include  # new
from django.conf.urls.static import static  # new


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
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #new
