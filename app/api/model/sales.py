# sales models


class Sale:
    """
    defines the sales model
    """
    def __init__(self, sale_id, product_name, quantity,
                 price_per_unit, total_price, sale_by):
        self.sale_id = sale_id
        self.product_name = product_name
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        self.total_price = total_price
        self.sale_by = sale_by

    def display_sales(self):
        """
        Sales entry in json
        :return:
        """
        return {
            'sale_id': self.sale_id,
            'product_name': self.product_name,
            'quantity': self.quantity,
            'price_per_unit': self.price_per_unit,
            'total_price': self.total_price,
            'sale_by': self.sale_by
        }
