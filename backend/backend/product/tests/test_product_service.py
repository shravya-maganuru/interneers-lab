import unittest
from unittest.mock import patch, MagicMock
from product.Services.product_service import ProductService


class TestProductService(unittest.TestCase):
    def setUp(self):
        self.service = ProductService()

    @patch('product.Services.product_service.create_product')
    def test_add_product(self, mock_create):
        mock_create.return_value = {'name': 'Test Product'}
        result = self.service.add_product({'name': 'Test Product'})
        self.assertEqual(result, {'name': 'Test Product'})
        mock_create.assert_called_once()

    @patch('product.Services.product_service.get_all_products')
    def test_list_products(self, mock_get_all):
        mock_get_all.return_value = [{'name': 'Test Product'}]
        result = self.service.list_products()
        self.assertEqual(len(result), 1)
        mock_get_all.assert_called_once()

    @patch('product.Services.product_service.get_product_by_id')
    def test_get_product(self, mock_get_by_id):
        mock_get_by_id.return_value = {'name': 'Test Product'}
        result = self.service.get_product('some_id')
        self.assertEqual(result['name'], 'Test Product')
        mock_get_by_id.assert_called_once_with('some_id')

    @patch('product.Services.product_service.update_product')
    def test_modify_product(self, mock_update):
        mock_update.return_value = {'name': 'Updated Product'}
        result = self.service.modify_product('prod123', {'name': 'Updated Product'})
        self.assertEqual(result['name'], 'Updated Product')
        mock_update.assert_called_once_with('prod123', {'name': 'Updated Product'})

    @patch('product.Services.product_service.delete_product')
    def test_remove_product(self, mock_delete):
        mock_delete.return_value = True
        result = self.service.remove_product('prod123')
        self.assertTrue(result)
        mock_delete.assert_called_once_with('prod123')

    @patch('product.Services.product_service.get_products_by_category')
    def test_list_products_by_category(self, mock_get_by_cat):
        mock_get_by_cat.return_value = [{'name': 'Product in Cat'}]
        result = self.service.list_products_by_category('cat123')
        self.assertEqual(len(result), 1)
        mock_get_by_cat.assert_called_once_with('cat123')
