# sales endpoints
from flask import request
from flask_restplus import Resource


from ..utils.dto import SalesDto
from ..service.sales import save_new_sale_order_items, get_by_sale_order_items_id, get_all_sale_order_items

api = SalesDto.api
_sale = SalesDto.sales


@api.route('/sales')
class SalesList(Resource):
    """Class that defines the routes for product related HTTP methods"""

    @api.response(200, 'Showing sales')
    @api.doc('list_of_sales')
    @api.marshal_list_with(_sale, envelope='sales')
    def get(self):
        """List all the sale order items"""
        return get_all_sale_order_items()

    @api.response(201, 'Sale order registered success')
    @api.doc('Create new sale order items')
    @api.expect(_sale, validate=True)
    def post(self):
        """Creates new sale order items"""
        data = request.json
        return save_new_sale_order_items(data=data)


@api.route('/sales/<int:sale_order_items_id>')
@api.param('sale_order_items_id', 'The sale order items identifier')
@api.response(404, 'Sale order item not found.')
class Sales(Resource):
    @api.doc('get a sale order item')
    @api.marshal_with(_sale)
    def get(self, sale_order_items_id):
        """get a sale order given its identifier"""
        sale_order_item = get_by_sale_order_items_id(sale_order_items_id)

        # Show an error message if no sale order item found with that id
        # else returns the sale order item
        if not sale_order_item:
            api.abort(404)
        else:
            return sale_order_item
