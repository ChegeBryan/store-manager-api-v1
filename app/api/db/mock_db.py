from app.api.model.products import Product


class MockDb:
    """
    Class that hold methods that will help in mock database manipulation
    """
    PRODUCTS = []
    SALES = []

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

    @classmethod
    def get_sale_by_id(cls, _id):
        """
        Loops through contents in the Sale list checking for an id match
        :param _id: sale identifier
        :return: sale with a certain id
        """
        for product in cls.SALES:
            if product.display_sales()['sale_id'] == _id:
                return product
