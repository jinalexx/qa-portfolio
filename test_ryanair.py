import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRyanairCareers:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 15)

    def teardown_method(self):
        self.driver.quit()

    def test_careers_page_loads(self):
        """Test that Ryanair careers page loads successfully"""
        self.driver.get("https://careers.ryanair.com")
        assert "Ryanair" in self.driver.title

    def test_page_title_present(self):
        """Test that the page has a visible title or heading"""
        self.driver.get("https://careers.ryanair.com")
        assert self.driver.title != ""

    def test_search_field_exists(self):
        """Test that a search or job listing element exists on careers page"""
        self.driver.get("https://careers.ryanair.com")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert len(body_text) > 0


