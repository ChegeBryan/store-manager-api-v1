# Products endpoints

from flask import request
from flask_restplus import Resource


from ..utils.dto import ProductDto
from ..service.products import save_new_product, get_all_products

api = ProductDto.api
_product = ProductDto.product


@api.route('/products')
class ProductList(Resource):
    """Class that defines the routes for product related HTTP methods"""

    @api.response(200, 'Showing products in store')
    @api.doc('list_of_products')
    @api.marshal_list_with(_product, envelope='products')
    def get(self):
        """List all products"""
        return get_all_products()

    @api.response(201, 'Product registered success')
    @api.doc('create a new product')
    @api.expect(_product, validate=True)
    def post(self):
        """Creates new product"""
        data = request.json
        return save_new_product(data=data)
