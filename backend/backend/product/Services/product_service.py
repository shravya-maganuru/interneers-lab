from ..Repositories.product_repository import (
    create_product, get_all_products, get_product_by_id, update_product, delete_product, get_products_by_category
)

def add_product(data):
    """Service function to add a product."""
    return create_product(data)

def list_products():
    """Service function to get all products."""
    return get_all_products()

def get_product(product_id):
    """Service function to get a single product."""
    return get_product_by_id(product_id)

def modify_product(product_id, data):
    """Service function to update a product."""
    return update_product(product_id, data)

def remove_product(product_id):
    """Service function to delete a product."""
    return delete_product(product_id)

def list_products_by_category(category_id):
    """Fetch products belonging to a specific category."""
    return get_products_by_category(category_id)