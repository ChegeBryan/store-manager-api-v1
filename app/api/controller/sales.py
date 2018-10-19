# sales endpoints
from flask import request
from flask_restplus import Resource


from ..utils.dto import SalesDto
from ..service.sales import save_new_sale, get_by_sale_id, get_all_sales

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
        return get_all_sales()

    @api.response(201, 'Sale order registered success')
    @api.doc('Create new sale order items')
    @api.expect(_sale, validate=True)
    def post(self):
        """Creates new sale order items"""
        data = request.json
        return save_new_sale(data=data)


@api.route('/sales/<int:sale_id>')
@api.param('sale_id', 'The sale order items identifier')
@api.response(404, 'Sale order item not found.')
class Sales(Resource):
    @api.doc('get a sale order item')
    @api.marshal_with(_sale)
    def get(self, sale_id):
        """get a sale order given its identifier"""
        sale_item = get_by_sale_id(sale_id)

        # Show an error message if no sale order item found with that id
        # else returns the sale order item
        if not sale_item:
            api.abort(404)
        else:
            return sale_item
