import uuid
from django.db import models

from companies.models import Company
from products.models import Product


class Order(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  created_at = models.DateTimeField(auto_now_add=True)
  company = models.ForeignKey(Company, on_delete=models.CASCADE)
  products = models.ManyToManyField(Product, through='OrderProduct')
  total_price = models.DecimalField(max_digits=10000, decimal_places=2, default=0.0)
  
  def __str__(self) -> str:
    return f"Order #{self.id} for {self.company.name}"
  
  def calculate_total_price(self):
    total_price = sum(item.quantity * item.product.price for item in self.order_items.all())
  

class OrderProduct(models.Model):
  order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField(default=1)
  
  def __str__(self):
        return f"{self.product.name} in Order #{self.order.id}"