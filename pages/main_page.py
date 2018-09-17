"""
Main Page Classes
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from elements.search_elements import SearchTextElement


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    GO_BUTTON = (By.ID, 'submit')

    search_text_element = SearchTextElement()

    def load(self):
        self.driver.get("http://www.python.org")

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return "Python" in self.driver.title

    def click_go_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*self.GO_BUTTON)
        element.click()
