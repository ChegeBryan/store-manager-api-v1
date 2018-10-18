# carry data between processes and marshalling data for API calls
from flask_restplus import Namespace, fields


class ProductDto:
    api = Namespace('product', description='product related operations')
    product = api.model('product', {
        'product_name': fields.String(required=True, description='product name'),
        'mini_description': fields.String(required=True, description='short product description'),
        'description': fields.String(required=True, description='detailed product description'),
        'price_per_unit': fields.Integer(required=True, description='price of one unit of the this product')
    })
