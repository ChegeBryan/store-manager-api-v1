import unittest
from app import create_app
from app.api.db.mock_db import PRODUCTS


class ProductApiTestCase(unittest.TestCase):
    """
    Class for  product endpoints cases
    """
    def setUp(self):
        """
        Defines the product variables and initializes app
        """
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.product = {
            "product_id": 1,
            "product_name": "Macbook 2017",
            "mini_description": "Macbook 2017, retina display",
            "description": "Macbook 2017, retina display, 16 GB Ram, 512 GB",
            "price_per_unit": 99999,
            "quantity_in_stock": 3,
            "stock_low_level_at": 6
        }

    def test_api_create_entry(self):
        """
        Test api can create a product (POST Request)
        :return: 201 Status code
        """
        response = self.client.post(
            '/api/v1/products',
            json=self.product
        )
        self.assertEqual(response.status_code, 201)

    def test_api_get_all_entry(self):
        """
        Test api can get all product entries (GET Request)
        :return: 200 Ok
        """
        response = self.client.get(
            '/api/v1/products',
            json=self.product
        )
        self.assertEqual(response.status_code, 200)

    def test_api_can_get_a_product_by_id(self):
        """
        Test api can get a single entry by id (GET Request)
        :return: 200 Ok
        """
        response = self.client.get(
            '/api/v1/products/1',
            json=self.product
        )
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        PRODUCTS[:] = []


