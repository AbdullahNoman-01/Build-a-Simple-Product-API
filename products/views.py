from .serializers import Product_Serializer
from rest_framework import generics
from .models import Product
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication

# get and post
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = Product_Serializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]