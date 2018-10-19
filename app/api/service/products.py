# defines the logic for the products model
from app.api.db import mock_db
from app.api.model.products import Product


def save_new_product(data):
    """Saves creation of new product if a product with the same doesnt exist"""

    new_product = Product(
        product_id=data['product_id'],
        product_name=data['product_name'],
        mini_description=data['mini_description'],
        description=data['description'],
        price_per_unit=data['price_per_unit'],
        quantity_in_stock=data['quantity_in_stock'],
        stock_low_alert_at=data['stock_low_alert_at']
    )
    save_changes(new_product)
    response_object = {
        'status': 'success',
        'message': 'Product added to catalog.'
    }
    return response_object, 201


def get_all_products():
    """
    this method gets returns all the products in the product list
    :return: list of all products
    """
    return mock_db.PRODUCTS, 200


def get_by_product_id(product_id):
    """
    method returns a single product in the product list
    :param product_id: the key to identify the product to return
    :return: single product
    """
    product = [product for product in mock_db.PRODUCTS if product['product_id'] == product_id]
    return product


def save_changes(data):
    """
    Save the single products inside the product list making a list of dictionaries
    :param data:
    """
    mock_db.PRODUCTS.append(data)
