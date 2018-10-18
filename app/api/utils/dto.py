# carry data between processes and marshalling data for API calls
from flask_restplus import Namespace, fields


class ProductDto:
    api = Namespace('product', description='product related operations')
    product = api.model('product', {
        'product_name': fields.String(required=True, description='product name'),
        'mini_description': fields.String(required=True, description='product description'),
        'description': fields.String(required=True, description='product name'),
        'price_per_unit': fields.Integer(required=True, description='product description')
    })
