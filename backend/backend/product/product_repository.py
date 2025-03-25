from mongoengine import Document, StringField, DecimalField, IntField, FloatField
from bson import ObjectId

class Product(Document):
    name = StringField(max_length=255, required=True)
    description = StringField()
    category = StringField(max_length=50)
    price = FloatField(required=True)
    brand = StringField(max_length=100)
    quantity = IntField(min_value=0)

    meta = {'collection': 'products'}  # This defines the MongoDB collection name

def create_product(data):
    """Creates a new product in MongoDB."""
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

