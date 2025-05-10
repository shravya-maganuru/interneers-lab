from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

# For Product Model
from .serializers import ProductSerializer
from .Services.product_service import add_product, list_products, get_product, modify_product, remove_product, list_products_by_category

# For ProductCategory Model
from .serializers import ProductCategorySerializer
from .Services.product_category_service import (
    add_category, list_categories, get_category, modify_category, remove_category
)

class ProductViewSet(viewsets.ViewSet):
    """
    A viewset to handle CRUD operations for products using MongoDB.
    """

    def list(self):
        """List all products."""
        products = list_products()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Create a new product."""
        try:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                product = add_product(serializer.validated_data)
                return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def retrieve(self, request, pk=None):
        """Retrieve a single product by ID."""
        product = get_product(pk)
        if product:
            return Response(ProductSerializer(product).data)
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        """Update a product."""
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            updated_product = modify_product(pk, serializer.validated_data)
            if updated_product:
                return Response(ProductSerializer(updated_product).data)
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Delete a product."""
        success = remove_product(pk)
        if success:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    
    """To access a product of a specific category"""

    @action(detail=False, methods=['get'], url_path='category/(?P<category_id>[^/.]+)')
    def by_category(self, request, category_id=None):
        """Fetch products belonging to a specific category."""
        products = list_products_by_category(category_id)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'], url_path='assign-category/(?P<category_id>[^/.]+)')
    def assign_category(self, request, pk=None, category_id=None):
        """Assign a product to a category."""
        product = modify_product(pk, {'category': category_id})
        if product:
            return Response(ProductSerializer(product).data)
        return Response({"error": "Product or Category not found"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['post'], url_path='remove-category')
    def remove_category(self, request, pk=None):
        """Remove a product from its category."""
        product = modify_product(pk, {'category': None})
        if product:
            return Response(ProductSerializer(product).data)
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

class ProductCategoryViewSet(viewsets.ViewSet):
    """
    A viewset to handle CRUD operations for product categories using MongoDB.
    """

    def list(self, request):
        """List all product categories."""
        categories = list_categories()
        serializer = ProductCategorySerializer(categories, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Create a new product category."""
        try:
            serializer = ProductCategorySerializer(data=request.data)
            if serializer.is_valid():
                category = add_category(serializer.validated_data)
                return Response(ProductCategorySerializer(category).data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        """Retrieve a single product category by ID."""
        category = get_category(pk)
        if category:
            return Response(ProductCategorySerializer(category).data)
        return Response({"error": "Product category not found"}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        """Update a product category."""
        serializer = ProductCategorySerializer(data=request.data)
        if serializer.is_valid():
            updated_category = modify_category(pk, serializer.validated_data)
            if updated_category:
                return Response(ProductCategorySerializer(updated_category).data)
            return Response({"error": "Product category not found"}, status=status.HTTP_400_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Delete a product category."""
        success = remove_category(pk)
        if success:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Product category not found"}, status=status.HTTP_404_NOT_FOUND)