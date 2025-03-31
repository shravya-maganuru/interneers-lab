from rest_framework_mongoengine.serializers import DocumentSerializer
from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import Product, ProductCategory

# Custom validator function
def validate_non_empty_brand(value):
    """Ensures the brand field is not empty or just whitespace."""
    if not value.strip():  # Prevents blank or whitespace-only values
        raise ValidationError("Brand cannot be empty.")
    return value

class ProductSerializer(DocumentSerializer): 

    name = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False)
    category = serializers.CharField(max_length=50, required=False)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=0)
    brand = serializers.CharField(max_length=50, required=True,validators=[validate_non_empty_brand])
    quantity = serializers.IntegerField(min_value=0)
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'price', 'brand', 'quantity']

class ProductCategorySerializer(DocumentSerializer):
    
    title = serializers.CharField(max_length = 100)
    description = serializers.StringField()

    class Meta:
        model = ProductCategory
        fields = ['id', 'title', 'description']
