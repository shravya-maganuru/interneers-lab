from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    for creating, reading, updating, and deleting products.
    """
    queryset = Product.objects.all().order_by('-id')  # Fetch all products, newest first
    serializer_class = ProductSerializer
