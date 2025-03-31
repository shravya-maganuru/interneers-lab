from mongoengine import Document, StringField, DecimalField, IntField, ReferenceField

class ProductCategory(Document):
    title = StringField(max_length=100, required=True, unique=True)
    description = StringField()

    meta = {'collection': 'product_categories'} 

    def __str__(self):
        return self.title
    
class Product(Document):
    name = StringField(required=True, max_length=255)
    description = StringField()
    category = ReferenceField(ProductCategory, required=True)
    price = DecimalField(precision=2, required=True)
    brand = StringField(max_length=100, required=True)
    quantity = IntField(min_value=0)

    meta = {'collection': 'products'}

    def __str__(self):
        return self.name
    
