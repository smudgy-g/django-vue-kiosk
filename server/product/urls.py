from django.urls import path, include
from product import views


urlpatterns = [
  path('products/', views.ProductList.as_view()),
  path('products/<uuid:product_id>', views.ProductDetail.as_view()),
]
