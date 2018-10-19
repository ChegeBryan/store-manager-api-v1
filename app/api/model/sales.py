# sales models


class SaleOrderItems:
    """
    defines the sales model
    """
    def __init__(self, sale_order_items_id, product_id, quantity,
                 price_per_unit, sale_order_id, user_id):
        self.sale_order_items_id = sale_order_items_id
        self.product_id = product_id
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        self.total_price = price_per_unit * quantity
        self.sale_order_id = sale_order_id
        self.user_id = user_id

