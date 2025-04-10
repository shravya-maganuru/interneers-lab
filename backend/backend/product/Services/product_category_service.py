from mongoengine.errors import ValidationError, DoesNotExist, NotUniqueError, OperationError
from product.Repositories.product_category_repository import (
    create_category,
    get_all_categories,
    get_category_by_id,
    update_category,
    delete_category
)


class ProductCategoryService:
    def add_category(self, data):
        """Service function to add a product category."""
        try:
            return create_category(data)
        except ValidationError as e:
            raise ValueError(f"Invalid category data: {e}")
        except NotUniqueError:
            raise ValueError("A category with this title already exists.")
        except OperationError as e:
            raise RuntimeError(f"Database operation failed: {e}")

    def list_categories(self):
        """Service function to get all product categories."""
        return get_all_categories()

    def get_category(self, category_id):
        """Service function to get a single category."""
        try:
            category = get_category_by_id(category_id)
            if not category:
                raise DoesNotExist("Category not found")
            return category
        except DoesNotExist:
            return None
        except Exception as e:
            raise RuntimeError(f"Error fetching category: {e}")

    def modify_category(self, category_id, data):
        """Service function to update a category."""
        try:
            category = update_category(category_id, data)
            if not category:
                raise DoesNotExist("Category not found")
            return category
        except ValidationError as e:
            raise ValueError(f"Invalid category data: {e}")
        except DoesNotExist:
            return None
        except OperationError as e:
            raise RuntimeError(f"Database operation failed: {e}")

    def remove_category(self, category_id):
        """Service function to delete a category."""
        try:
            success = delete_category(category_id)
            if not success:
                raise DoesNotExist("Category not found")
            return success
        except DoesNotExist:
            return None
        except Exception as e:
            raise RuntimeError(f"Error deleting category: {e}")