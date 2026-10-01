from django.urls import path
from .import views

urlpatterns = [
   path('products/', views.ProductListCreateAPIView.as_view(), name='product-list-create'),
]
