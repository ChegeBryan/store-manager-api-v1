# product models


class Product:
    """Defines the user model"""
    def __init__(self, product_id, product_name,
                 mini_description, description,
                 price_per_unit, quantity_in_stock,
                 stock_low_alert_at):
        self.product_id = product_id
        self.product_name = product_name
        self.mini_description = mini_description
        self.description = description
        self.price_per_unit = price_per_unit
        self.quantity_in_stock = quantity_in_stock
        self.stock_low_alert_at = stock_low_alert_at

    def display_product(self):
        """
        Product entry in json
        :return:
        """
        return {
            'product_id': self.product_id,
            'product_name': self.product_name,
            'mini_description': self.mini_description,
            'description': self.description,
            'price_per_unit': self.price_per_unit,
            'quantity_in_stock': self.quantity_in_stock,
            'stock_low_alert_at': self.stock_low_alert_at
        }


