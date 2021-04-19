"""
Base page module
"""


class BasePage:  # pylint: disable=too-few-public-methods
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver
