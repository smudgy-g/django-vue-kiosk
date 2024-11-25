from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from .serialisers import ProductSerialiser

class ProductList(APIView):
  def get(self, request, format=None):
    products = Product.objects.all()
    serialiser = ProductSerialiser(products, many=True)
    return Response(serialiser.data)