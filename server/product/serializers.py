from rest_framework import serializers

from ..supplier.serializers import SupplierSerializer

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
  supplier = SupplierSerializer()
  
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

  