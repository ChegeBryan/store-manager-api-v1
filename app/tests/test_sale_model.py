# Test sale model

import unittest

from app.api.model.sales import SaleOrderItems
from app.api.db.mock_db import SALEITEMS
from app.api.service.sales import save_changes


class TestSaleModel(unittest.TestCase):
    """
    Test class that defines test cases for the Sale class behaviours
    """
    def setUp(self):
        """
        Set up a flask sale_order_items
        :arg sale_order_items_ID, product id, quantity, price_per_unit, sale_order_id,
        user_id, price_total
        """
        self.new_sale_order_items = SaleOrderItems(
            1, 2, 4, 1000, 1, 2
        )

    def test_sale_order_items_object_creation(self):
        """
        test_init test case tests if the ne object is initialized properly
        """
        self.assertEqual(self.new_sale_order_items.sale_order_items_id, 1)
        self.assertEqual(self.new_sale_order_items.product_id,2)
        self.assertEqual(self.new_sale_order_items.quantity, 4)
        self.assertEqual(self.new_sale_order_items.price_per_unit, 1000)
        self.assertEqual(self.new_sale_order_items.total_price, 4000)
        self.assertEqual(self.new_sale_order_items.sale_order_id, 1)
        self.assertEqual(self.new_sale_order_items.user_id, 2)

    def test_save_sale_order_items(self):
        save_changes(self.new_sale_order_items)
        self.assertEqual(len(SALEITEMS), 1)

    def test_save_multiple_sale_order_items(self):
        """
        test_save_multiple_sale_order_items to check if we save multiple
        objects to our SaleOrderItems
        """

        save_changes(self.new_sale_order_items)
        test_sale_order_items = SaleOrderItems(1, 2, 4, 1000, 1, 2)  # new sale order item
        save_changes(test_sale_order_items)
        self.assertEqual(len(SALEITEMS), 2)

    def tearDown(self):
        SALEITEMS[:] = []


