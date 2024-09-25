from django.urls import path
from .views import ProductListCreateApiView, ProductDetailAPIView

urlpatterns = [
    path('products/', ProductListCreateApiView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
]