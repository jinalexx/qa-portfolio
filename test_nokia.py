import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestNokiaCareers:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 15)

    def teardown_method(self):
        self.driver.quit()

    def test_careers_page_loads(self):
        """Test that Nokia careers page loads successfully"""
        self.driver.get("https://www.nokia.com/about-us/careers/")
        assert "Nokia" in self.driver.title

    def test_page_title_present(self):
        """Test that the page has a visible title"""
        self.driver.get("https://www.nokia.com/about-us/careers/")
        assert self.driver.title != ""

    def test_careers_content_exists(self):
        """Test that careers page has visible content"""
        self.driver.get("https://www.nokia.com/about-us/careers/")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert len(body_text) > 0