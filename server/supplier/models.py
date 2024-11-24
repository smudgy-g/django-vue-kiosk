from django.db import models


class Supplier(models.Model):
  id = models.UUIDField(auto_created=True, primary_key=True)
  name = models.CharField(max_length=50)
  

  def __str__(self) -> str:
    return self.name