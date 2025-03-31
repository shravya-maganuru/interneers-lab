from mongoengine import Document, StringField, DecimalField, IntField, FloatField
from bson import ObjectId

def create_product(data):
    """Defining a new MongoDB project."""
    try:
        product = Product(**data)
        product.save()
        return product
    except Exception as e:
        print(f"Error creating product: {e}")
        raise

def get_all_products():
    """Fetches all products."""
    return Product.objects()

def get_product_by_id(product_id):
    """Fetch a single product by its ID."""
    try:
        if not ObjectId.is_valid(product_id):  # Check if it's a valid ObjectId
            return None
        return Product.objects(id=ObjectId(product_id)).first()
    except Exception as e:
        print(f"Error fetching product: {e}")
        return None

def update_product(product_id, data):
    """Update a product by its ID."""
    product = get_product_by_id(product_id)
    if product:
        product.update(**data)
        return product.reload()  # Ensure the updated product is returned
    return None

def delete_product(product_id):
    """Deletes a product by its ID."""
    product = get_product_by_id(product_id)
    if product:
        product.delete()
        return True
    return False

"""Connected with ProductCategory layer"""
def get_products_by_category(category_id):
    """Fetch products that belong to a given category."""
    return Product.objects(category=category_id)