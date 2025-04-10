from mongoengine import connect
from product.models import Product, ProductCategory

def seed():
    connect("seed_test", host="mongodb://localhost:27017/")

    # Clear existing data
    Product.objects.delete()
    ProductCategory.objects.delete()

    # Add seed categories
    electronics = ProductCategory(title="Electronics", description="Electronic gadgets")
    clothing = ProductCategory(title="Clothing", description="Apparel and accessories")
    electronics.save()
    clothing.save()

    # Add seed products
    Product(title="Smartphone", description="Android smartphone", price=599.99, category=electronics).save()
    Product(title="Jeans", description="Blue denim", price=39.99, category=clothing).save()

    print("Seeded Products and Categories!")

if __name__ == "__main__":
    seed()
