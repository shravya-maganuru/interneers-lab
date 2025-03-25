from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .product_service import add_product, list_products, get_product, modify_product, remove_product

class ProductViewSet(viewsets.ViewSet):
    """
    A viewset to handle CRUD operations for products using MongoDB.
    """

    def list(self, request):
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