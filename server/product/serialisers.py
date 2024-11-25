from rest_framework import serializers

from .models import Product

class ProductSerialiser(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = (
      'id',
      'supplier',
      'created_at',
      'name',
      'price',
      'description',
      'product_code',
    )