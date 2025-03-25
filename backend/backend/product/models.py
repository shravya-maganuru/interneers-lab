from mongoengine import Document, StringField, DecimalField, IntField

class Product(Document):
    name = StringField(required=True, max_length=255)
    description = StringField()
    category = StringField(max_length=50)
    price = DecimalField(precision=2, required=True)
    brand = StringField(max_length=100)
    quantity = IntField(min_value=0)

    def __str__(self):
        return self.name
