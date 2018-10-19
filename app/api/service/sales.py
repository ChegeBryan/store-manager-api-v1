# defines the logic for the sales model

from app.api.db import mock_db
from app.api.model.sales import SaleOrderItems


def save_new_sale_order_items(data):
    """
    saves the creation of a new sale order items
    :param data: form input
    :return:
    """

    new_sale_order_items = SaleOrderItems(
        sale_order_items_id=data['sale_order_items_id'],
        product_id=data['product_name'],
        quantity=data['quantity'],
        price_per_unit=data['price_per_unit'],
        sale_order_id=data['sale_order_id'],
        user_id=data['user_id']
    )
    save_changes(new_sale_order_items)
    response_object = {
        'status': 'success',
        'message': 'Sale order item recorded.'
    }
    return response_object, 201


def get_all_sale_order_items():
    """
    this method gets and returns all the sale-order-items in the saleitems list
    :return:
    """
    return mock_db.SALEITEMS, 200


def save_changes(data):
    """
    save the single sale order items making a list of dictionaries
    """
    mock_db.SALEITEMS.append(data)