from rest_framework import serializers
from .models import Supplier

class SupplierSerializer(serializers.ModelSerializer):
  class Meta:
    model = Supplier
    fields = (
      'id',
      'name',
      'email',
      'phone',
      'contact_person',
      'notes',
    )