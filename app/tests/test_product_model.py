# Test product model

import unittest

from app.api.model.products import Product
from app.api.db.mock_db import MockDb
from app.api.service.products import save_changes


class TestProductModel(unittest.TestCase):
    """
    Test class that defines test cases for the Product class behaviours.
    """
    def setUp(self):
        self.new_product = Product(1, 'product name', 'mini description',
                                   'description', 234, 4, 3)

    def test_product_object_creation(self):
        """
        test_init test case to test if the object is initialized properly
        :return:
        """
        self.assertEqual(self.new_product.product_id, 1)

    def test_product_saved(self):
        save_changes(self.new_product)
        self.assertEqual(len(MockDb.PRODUCTS), 1)

    def tearDown(self):
        MockDb.PRODUCTS[:] = []
