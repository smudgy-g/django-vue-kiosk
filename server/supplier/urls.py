from django.urls import path
from supplier import views

urlpatterns = [
  path('suppliers/', views.SupplierList.as_view())
]