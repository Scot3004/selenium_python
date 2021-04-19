"""
Search page
"""

from pages.base_page import BasePage


class SearchResultsPage(BasePage):  # pylint: disable=too-few-public-methods
    """Search results page action methods come here"""

    def is_results_found(self):
        """
        Probably should search for this text in the specific page
        element, but as for now it works fine
        :return:
        """
        return "No results found." not in self.driver.page_source
