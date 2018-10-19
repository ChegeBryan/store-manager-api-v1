# sales endpoints
from flask import request
from flask_restplus import Resource


from ..utils.dto import SalesDto
from ..service.sales import save_new_sale_order_items,save_changes, get_by_sale_order_items_id, get_all_sale_order_items

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
