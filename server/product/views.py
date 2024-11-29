from django.http import Http404
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

class ProductList(APIView):
  def get(self, request, format=None):
    products = Product.objects.all()
    serialiser = ProductSerializer(products, many=True)
    return Response(serialiser.data)
  
class ProductDetail(APIView):
  def get_object(self, product_id):
    try:
      return Product.objects.get(id=product_id)
    except Product.DoesNotExist:
      raise Http404
    
  def get(self, request, product_id, format=None):
    product = self.get_object(product_id)
    serialiser = ProductSerialiser(product)
    return Response(serialiser.data)