"""
Base test module
"""

import unittest

from selenium import webdriver


class BaseTest(unittest.TestCase):
    """Class which all selenium test should inherit"""

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close()
