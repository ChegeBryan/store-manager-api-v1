# defines the logic for the products model
from app.api.db import mock_db
from app.api.model.products import Product


def save_new_product(data):
    """Saves creation of new product if a product with the same doesnt exist"""

    new_product = Product(
        product_id=mock_db.PRODUCTS[-1]['product_id'] + 1,
        product_name=data['product_name'],
        mini_description=data['mini_description'],
        description=data['description'],
        price_per_unit=data['price_per_unit']
    )
    save_changes(new_product)
    response_object = {
        'status': 'success',
        'message': 'Product added to catalog.'
    }
    return response_object, 201


def get_all_products():
    return mock_db.PRODUCTS, 200


def save_changes(data):
    mock_db.PRODUCTS.append(data)
