import uuid

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  name = models.CharField(max_length=100)
  street_address = models.CharField(max_length=200)
  city = models.CharField(max_length=100)
  region = models.CharField(max_length=100)
  zip = models.CharField(max_length=10)
  
  def __str__(self) -> str:
    return f"{self.user.username}'s company profile"