from rest_framework import serializers

from .models import Supplier

class SupplierSerializer(serializers.Serializer):
  class Meta:
    model = Supplier
    fields = (
      'id',
      'company',
      'name',
      'email',
      'phone',
      'contact_person',
      'notes',
    )