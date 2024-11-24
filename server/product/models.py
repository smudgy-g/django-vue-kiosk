from django.db import models


class Product(models.Model):
  id = models.UUIDField(auto_created=True, primary_key=True)
  name = models.CharField(max_length=50)
  product_code = models.CharField(max_length=50, blank=True, null=True)
  price = models.DecimalField(decimal_places=2, max_digits=10, blank=True)
  description = models.CharField(max_length=250, blank=True, null=True)

  def __str__(self) -> str:
    return self.name