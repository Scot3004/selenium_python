"""
Test Case
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from tests.base_test import BaseTest


class TestPythonOrgSearchNoPOM(BaseTest):
    """A sample test class to show how page object works"""

    def test_search_in_python_org(self):
        """
        Tests python.org search feature.
        Searches for the word "pycon" then verified that some results show up.
        Note that it does not look for any particular text in search results page.
        This test verifies that the results were not empty.
        """

        self.driver.get("http://www.python.org")
        # Checks if the word "Python" is in title
        assert "Python" in self.driver.title, "python.org title doesn't match."
        # Sets the text of search textbox to "pycon"
        search_locator = 'q'
        WebDriverWait(self.driver, 100).until(
            lambda driver: driver.find_element_by_name(search_locator))
        self.driver.find_element_by_name(search_locator).clear()
        self.driver.find_element_by_name(search_locator).send_keys("pycon")
        self.driver.find_element(By.ID, 'submit').click()
        # Verifies that the results page is not empty
        assert "No results found." not in self.driver.page_source, "No results found."
