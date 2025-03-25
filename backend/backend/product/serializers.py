from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import Product

class ProductSerializer(DocumentSerializer):  
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'price', 'brand', 'quantity']
