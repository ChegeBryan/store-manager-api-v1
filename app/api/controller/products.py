# Products endpoints

from flask import request
from flask_restplus import Resource


from ..utils.dto import ProductDto
from ..service.products import save_new_product, get_all_products, get_by_product_id

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


@api.route('/products/<int:product_id>')
@api.param('product_id', 'The product identifier')
@api.response(404, 'Product not found.')
class Product(Resource):
    @api.doc('get a product')
    @api.marshal_with(_product)
    def get(self, product_id):
        """get a product given its identifier"""
        product = get_by_product_id(product_id)

        # Show an error message if no product found with that id
        # else returns the product
        if not product:
            api.abort(404)
        else:
            return product
