"""
Search text element
"""
from elements.base_element import BasePageElement


class SearchTextElement(BasePageElement): # pylint: disable=too-few-public-methods
    """This class gets the search text from the specified locator"""

    # The locator for search box where search string is entered
    locator = 'q'
