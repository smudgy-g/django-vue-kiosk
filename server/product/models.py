import uuid
from django.db import models

from supplier.models import Supplier


class Product(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  name = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=1000, decimal_places=2)
  description = models.CharField(max_length=500, null=True, blank=True)
  product_code = models.CharField(max_length=100, null=True, blank=True)

  class Meta:
    db_table = 'products'
    
  def __str__(self):
    return f"{self.name} distributed by {self.supplier.name}"