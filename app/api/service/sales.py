# defines the logic for the sales model

from app.api.db import mock_db
from app.api.model.sales import Sale


def save_new_sale(data):
    """
    saves the creation of a new sale order items
    :param data: form input
    :return:
    """

    new_sale = Sale(
        sale_id=data['sale_id'],
        product_name=data['product_name'],
        quantity=data['quantity'],
        price_per_unit=data['price_per_unit'],
        total_price=data['total_price'],
        sale_by=data['sale_by']
    )
    save_changes(new_sale)
    response_object = {
        'status': 'success',
        'message': 'Sale order item recorded.'
    }
    return response_object, 201


def get_all_sales():
    """
    this method gets and returns all the sale-items in the sale items list
    :return:
    """
    return mock_db.SALES, 200


def get_by_sale_id(sale_id):
    """
    method returns a single product in the product list
    :param sale_id: the key to identify the product to return
    :return: single product
    """
    item = [item for item in mock_db.SALES if item['sale_id'] == sale_id]
    return item


def save_changes(data):
    """
    save the single sale order items making a list of dictionaries
    """
    mock_db.SALES.append(data)
