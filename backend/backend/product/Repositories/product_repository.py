from mongoengine import Document, StringField, DecimalField, IntField, FloatField
from bson import ObjectId
from product.models import Product


class ProductService:
    def create_product(self, data):
        """Creates a new MongoDB product."""
        try:
            product = Product(**data)
            product.save()
            return product
        except Exception as e:
            print(f"Error creating product: {e}")
            raise

    def get_all_products(self):
        """Fetches all products."""
        return Product.objects()

    def get_product_by_id(self, product_id):
        """Fetch a single product by its ID."""
        try:
            if not ObjectId.is_valid(product_id):
                return None
            return Product.objects(id=ObjectId(product_id)).first()
        except Exception as e:
            print(f"Error fetching product: {e}")
            return None

    def update_product(self, product_id, data):
        """Update a product by its ID."""
        product = self.get_product_by_id(product_id)
        if product:
            product.update(**data)
            return product.reload()
        return None

    def delete_product(self, product_id):
        """Deletes a product by its ID."""
        product = self.get_product_by_id(product_id)
        if product:
            product.delete()
            return True
        return False

    def get_products_by_category(self, category_id):
        """Fetch products that belong to a given category."""
        return Product.objects(category=category_id)