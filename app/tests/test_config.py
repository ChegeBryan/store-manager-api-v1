# Test config.py

import unittest

from app import create_app


class TestConfig(unittest.TestCase):
    """
    Test app configures correctly in different environments
    """

    def test_app_is_development(self):
        app = create_app('development')
        self.assertTrue(app.config['DEBUG'] is True)

    def test_app_is_testing(self):
        app = create_app('testing')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertTrue(app.config['TESTING'] is True)

    def test_app_is_production(self):
        app = create_app('production')
        self.assertFalse(app.config['DEBUG'] is True)
        self.assertFalse(app.config['TESTING'] is True)





