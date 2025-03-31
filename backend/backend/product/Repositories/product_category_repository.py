from ..models import ProductCategory
from mongoengine.errors import ValidationError, DoesNotExist, NotUniqueError, OperationError
from bson import ObjectId

def create_category(data):
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

def get_all_categories():
    """Fetches all product categories."""
    return ProductCategory.objects()

def get_category_by_id(category_id):
    """Fetch a single product category by ID."""
    if not ObjectId.is_valid(category_id):
        return None
    try:
        return ProductCategory.objects.get(id=category_id)
    except DoesNotExist:
        return None

def update_category(category_id, data):
    """Update a product category by ID."""
    if not ObjectId.is_valid(category_id):
        return None

    updated_category = ProductCategory.objects(id=category_id).modify(
        set__title=data.get('title'),
        set__description=data.get('description'),
        new=True  # Return the updated document
    )
    return updated_category

def delete_category(category_id):
    """Deletes a product category by ID."""
    if not ObjectId.is_valid(category_id):
        return False
    deleted_count = ProductCategory.objects(id=category_id).delete()
    return deleted_count > 0
