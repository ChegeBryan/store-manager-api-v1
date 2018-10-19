# tests for sale api

import unittest
from app import create_app
from app.api.db.mock_db import SALEITEMS


class SalesApiTestCase(unittest.TestCase):
    """
    Class for testing sales endpoints
    """
    def setUp(self):
        """
        Defines the sale order variables and initializes the app
        """
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.sales_order_item = {
            'sale_order_items_id': 1,
            'product_id': 1,
            'quantity': 3,
            'price_per_unit': 1000,
            'sale_order_id': 3,
            'user_id': 1
        }

    def test_api_create_new_sale_order_item(self):
        """
        Test api can create a sales order item (POST Request)
        :return: 201 status code
        """
        response = self.client.post(
            '/api/v1/sales',
            json=self.sales_order_item
        )
        self.assertEqual(response.status_code, 201)

    def test_api_get_all_sales(self):
        """
        Test api can get all product entries (GET Request)
        :return: 200 OK
        """
        response = self.client.get(
            '/api/v1/sales',
            json=self.sales_order_item
        )
        self.assertEqual(response.status_code, 200)

    def test_api_can_get_a_sales_by_id(self):
        """
        Test api can get a single sale order by id (GET Request)
        :return: 200 Ok
        """
        response = self.client.get(
            '/api/v1/products/1',
            json=self.sales_order_item
        )
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        SALEITEMS[:] = []