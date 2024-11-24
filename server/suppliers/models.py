import uuid
from django.db import models

from companies.models import Company


class Supplier(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  company = models.ForeignKey(Company, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  name = models.CharField(max_length=100)
  email = models.CharField(max_length=50)
  phone = models.CharField(max_length=20, null=True, blank=True)
  contact_person = models.CharField(max_length=200, null=True, blank=True)
  notes = models.CharField(max_length=10000, null=True, blank=True)