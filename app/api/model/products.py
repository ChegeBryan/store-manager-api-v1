# product models


class Product:
    """Defines the user model"""
    def __init__(self, product_id, product_name,
                 mini_description, description,
                 price_per_quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.mini_description = mini_description
        self.description = description
        self.price_per_unit = price_per_quantity
        self.limited = False

