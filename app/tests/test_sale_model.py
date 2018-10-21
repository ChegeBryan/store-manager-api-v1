# Test sale model

import unittest

from app.api.model.sales import Sale
from app.api.db.mock_db import MockDb
from app.api.service.sales import save_changes


class TestSaleModel(unittest.TestCase):
    """
    Test class that defines test cases for the Sale class behaviours
    """
    def setUp(self):
        """
        Set up a flask sale_order_items
        :arg sale_id, product name, quantity, price_per_unit, total_price, sale_by,
        """
        self.new_sale = Sale(
            1, 'Macs', 4, 1000, 4000, 'me'
        )

    def test_sale_order_items_object_creation(self):
        """
        test_init test case tests if the ne object is initialized properly
        """
        self.assertEqual(self.new_sale.sale_id, 1)
        self.assertEqual(self.new_sale.product_name, 'Macs')
        self.assertEqual(self.new_sale.quantity, 4)
        self.assertEqual(self.new_sale.price_per_unit, 1000)
        self.assertEqual(self.new_sale.total_price, 4000)
        self.assertEqual(self.new_sale.sale_by, 'me')

    def test_save_sale(self):
        save_changes(self.new_sale)
        self.assertEqual(len(MockDb.SALES), 1)

    def test_save_multiple_sales(self):
        """
        test_save_multiple_sales to check if we save multiple
        objects to our Sale
        """

        save_changes(self.new_sale)
        test_sale = Sale(1, 'a toy', 4, 1000, 4000, 'me')  # new sale
        save_changes(test_sale)
        self.assertEqual(len(MockDb.SALES), 2)

    def tearDown(self):
        MockDb.SALES[:] = []


