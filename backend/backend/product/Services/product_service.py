from product.Repositories.product_repository import (
    create_product,
    get_all_products,
    get_product_by_id,
    update_product,
    delete_product,
    get_products_by_category
)


class ProductService:
    def add_product(self, data):
        """Service function to add a product."""
        return create_product(data)

    def list_products(self):
        """Service function to get all products."""
        return get_all_products()

    def get_product(self, product_id):
        """Service function to get a single product."""
        return get_product_by_id(product_id)

    def modify_product(self, product_id, data):
        """Service function to update a product."""
        return update_product(product_id, data)

    def remove_product(self, product_id):
        """Service function to delete a product."""
        return delete_product(product_id)

    def list_products_by_category(self, category_id):
        """Fetch products belonging to a specific category."""
        return get_products_by_category(category_id)