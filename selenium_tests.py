from selenium.webdriver.common.by import By

__author__ = 'drzewko'

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_google_page_redirects_to_encrypted_version_of_itself(self):
        driver = self.driver
        driver.get("http://www.google.com")
        self.assertIn("https://", driver.current_url)

    def test_google_contains_search_bar(self):
        driver = self.driver
        driver.get("http://www.google.com")
        driver.find_element_by_xpath("//input[@name='btnKx']")


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()