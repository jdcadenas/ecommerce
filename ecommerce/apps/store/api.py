import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from apps.cart.cart import Cart

from .models import Product
from django.shortcuts import get_object_or_404

from apps.cart.cart import Cart

from .models import Product

def api_add_to_cart(request):
  data=json.loads(request.body)
  jsonResponse = {'succes': True }
  product_id = data['product_id']
  update = data['update']
  quantity = data['quantity']
  
  print(data)
  print(data['product_id'])
  
  cart = Cart(request)
  print(cart)
  product = get_object_or_404(Product, pk=product_id)
  
  if not update:
    cart.add(product=product, quantity = 1, update_quantity=False)
  else:
    cart.add(product=product, quantity=quantity, update_quantity=True)
  
  return JsonResponse(jsonResponse)
def api_increment_quantity(request):
  data=json.loads(request.body)
  jsonResponse = {'succes': True }
  product_id = data['product_id']
  
  cart = Cart(request)
  
  
  
def api_remove_from_cart(request):
  data=json.loads(request.body)
  jsonResponse = {'succes': True }
  product_id = str(data['product_id'])
  
  cart = Cart(request)
  cart.remove(product_id)
  
  return JsonResponse(jsonResponse)