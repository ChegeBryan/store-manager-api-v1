from app.api.model.products import Product


class MockDb:
    """
    Class that hold methods that will help in mock database manipulation
    """
    PRODUCTS = []

    @classmethod
    def get_product_by_id(cls, _id):
        """
        Loops through contents in the Product list checking for an id match
        :param _id: product identifier
        :return: product with a certain id
        """
        for product in cls.PRODUCTS:
            if product.display_product()['product_id'] == _id:
                return product

SALES = [
    {
        "sale_id": 1,
        "product_name": 'Mac book 2017',
        "quantity": 2,
        "price_per_unit": 99,
        "total_price": 99999,
        "sold_by": 'bryan'

    },
    {
        "sale_id": 1,
        "product_name": 2,
        "quantity": 2,
        "price_per_unit": 34,
        "total_price": 2223,
        "sale_by": 'bryan'
    }
]