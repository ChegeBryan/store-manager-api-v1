import unittest
from app import create_app
from app.api.db.mock_db import PRODUCTS


class ProductApiTestCase(unittest.TestCase):
    """
    Class for  product endpoints cases
    """
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.product = {
            "product_id": 1,
            "product_name": "Macbook 2017",
            "mini_description": "Macbook 2017, retina dislay",
            "description": "Macbook 2017, retina display, 16 GB Ram, 512 GB",
            "price_per_unit": 99999,
            "limited": False
        }

    def test_api_create_entry(self):
        response = self.client.post(
            '/api/v1/products',
            json=self.product
        )
        self.assertEqual(response.status_code, 201)

    def test_api_get_all_entry(self):
        response = self.client.get(
            '/api/v1/products',
            json=self.product
        )
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        PRODUCTS[:] = []

