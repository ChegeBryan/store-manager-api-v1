# carry data between processes and marshalling data for API calls
from flask_restplus import Namespace, fields


class ProductDto:
    api = Namespace('product', description='product related operations')
    product = api.model('product', {
        'product_id': fields.Integer(required=True, description='product identifier'),
        'product_name': fields.String(required=True, description='product name'),
        'mini_description': fields.String(required=True, description='short product description'),
        'description': fields.String(required=True, description='detailed product description'),
        'price_per_unit': fields.Integer(required=True, description='price of one unit of the this product'),
        'quantity_in_stock': fields.Integer(required=True, description='quantity of this commodity in store'),
        'stock_low_alert_at': fields.Integer(required=True, description='quantity to alert when below')
    })


class SalesDto:
    api = Namespace('sales', description='sales related operations')
    sales = api.model('sales', {
        'sale_id': fields.Integer(required=True, description='sale identifier'),
        'product_name': fields.String(required=True, description='product identifier'),
        'quantity': fields.Integer(required=True, description='quantity of product ordered'),
        'price_per_unit': fields.Integer(required=True, description='1 unit price of commodity'),
        'total_price': fields.Integer(required=True, description='total price of the commodities purchased'),
        'sale_by': fields.String(required=True, description='user name for sale attendant')
    })
