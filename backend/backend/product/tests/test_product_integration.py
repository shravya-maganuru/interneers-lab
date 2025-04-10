import unittest
import json
from bson import ObjectId
from mongoengine import connect, disconnect
from rest_framework.test import APITestCase
from rest_framework import status
from product.models import Product, ProductCategory


class ProductIntegrationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connect("seed_test", host="mongodb://localhost:27017/")
        Product.objects.delete()
        ProductCategory.objects.delete()

    @classmethod
    def tearDownClass(cls):
        disconnect()

    def setUp(self):
        self.category = ProductCategory(title="Books", description="Educational and fiction").save()
        self.product = Product(
            title="Python 101",
            description="Beginner book for Python",
            price=29.99,
            category=self.category
        ).save()

    def tearDown(self):
        Product.objects.delete()
        ProductCategory.objects.delete()

    def test_product_creation(self):
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(self.product.title, "Python 101")

    def test_product_belongs_to_category(self):
        self.assertEqual(self.product.category.title, "Books")


class ProductCategoryProductIntegrationTest(APITestCase):
    def setUp(self):
        self.category_data = {
            "title": "Electronics",
            "description": "Devices and gadgets"
        }
        self.product_data = {
            "title": "Smartphone",
            "description": "Latest model with 5G",
            "price": 699.99,
            "quantity": 10
        }

    def test_full_category_product_flow(self):
        # 1. Create Category
        response = self.client.post("/categories/", self.category_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        category_id = response.data["id"]

        # 2. Get All Categories
        response = self.client.get("/categories/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        # 3. Get Category by ID
        response = self.client.get(f"/categories/{category_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.category_data["title"])

        # 4. Update Category
        updated_data = {"title": "Updated Electronics", "description": "Updated desc"}
        response = self.client.put(f"/categories/{category_id}/", updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Electronics")

        # 5. Create Product
        self.product_data["category"] = category_id
        response = self.client.post("/products/", self.product_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        product_id = response.data["id"]

        # 6. Get All Products
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        # 7. Get Products by Category
        response = self.client.get(f"/products/category/{category_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], self.product_data["title"])

        # 8. Delete Product
        response = self.client.delete(f"/products/{product_id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # 9. Delete Category
        response = self.client.delete(f"/categories/{category_id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


if __name__ == "__main__":
    unittest.main(verbosity=2)
