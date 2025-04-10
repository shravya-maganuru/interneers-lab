import unittest
from unittest.mock import patch, MagicMock
from product.Services.product_category_service import ProductCategoryService


class TestProductCategoryService(unittest.TestCase):
    def setUp(self):
        self.service = ProductCategoryService()

    @patch('product.Services.product_category_service.create_category')
    def test_add_category(self, mock_create):
        mock_create.return_value = {'title': 'Category 1'}
        result = self.service.add_category({'title': 'Category 1'})
        self.assertEqual(result['title'], 'Category 1')
        mock_create.assert_called_once()

    @patch('product.Services.product_category_service.get_all_categories')
    def test_list_categories(self, mock_get_all):
        mock_get_all.return_value = [{'title': 'Category 1'}]
        result = self.service.list_categories()
        self.assertEqual(len(result), 1)
        mock_get_all.assert_called_once()

    @patch('product.Services.product_category_service.get_category_by_id')
    def test_get_category(self, mock_get):
        mock_get.return_value = {'title': 'Category 1'}
        result = self.service.get_category('cat123')
        self.assertEqual(result['title'], 'Category 1')
        mock_get.assert_called_once_with('cat123')

    @patch('product.Services.product_category_service.update_category')
    def test_modify_category(self, mock_update):
        mock_update.return_value = {'title': 'Updated Cat'}
        result = self.service.modify_category('cat123', {'title': 'Updated Cat'})
        self.assertEqual(result['title'], 'Updated Cat')
        mock_update.assert_called_once_with('cat123', {'title': 'Updated Cat'})

    @patch('product.Services.product_category_service.delete_category')
    def test_remove_category(self, mock_delete):
        mock_delete.return_value = True
        result = self.service.remove_category('cat123')
        self.assertTrue(result)
        mock_delete.assert_called_once_with('cat123')

    @patch('product.Services.product_category_service.create_category')
    def test_add_category_raises_value_error(self, mock_create):
        from mongoengine.errors import ValidationError
        mock_create.side_effect = ValidationError("Invalid data")
        with self.assertRaises(ValueError):
            self.service.add_category({'title': ''})
