from mongoengine import Document, StringField
from mongoengine.errors import ValidationError, DoesNotExist, NotUniqueError, OperationError
from bson import ObjectId
from product.models import ProductCategory


class ProductCategoryService:
    def create_category(self, data):
        """Creates a new product category."""
        try:
            category = ProductCategory(**data)
            category.save()
            return category
        except ValidationError as e:
            raise ValueError(f"Invalid category data: {e}")
        except NotUniqueError:
            raise ValueError("A category with this title already exists.")
        except OperationError as e:
            raise RuntimeError(f"Database operation failed: {e}")

    def get_all_categories(self):
        """Fetches all product categories."""
        return ProductCategory.objects()

    def get_category_by_id(self, category_id):
        """Fetch a single product category by ID."""
        if not ObjectId.is_valid(category_id):
            return None
        try:
            return ProductCategory.objects.get(id=category_id)
        except DoesNotExist:
            return None

    def update_category(self, category_id, data):
        """Update a product category by ID."""
        if not ObjectId.is_valid(category_id):
            return None

        updated_category = ProductCategory.objects(id=category_id).modify(
            set__title=data.get('title'),
            set__description=data.get('description'),
            new=True  # Return the updated document
        )
        return updated_category

    def delete_category(self, category_id):
        """Deletes a product category by ID."""
        if not ObjectId.is_valid(category_id):
            return False
        deleted_count = ProductCategory.objects(id=category_id).delete()
        return deleted_count > 0