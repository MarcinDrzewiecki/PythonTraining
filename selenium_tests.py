from selenium.webdriver.common.by import By
import time
from selenium_test_do_it_right import OnBlankPage
from selenium_test_do_it_right import OnGooglePage

__author__ = 'drzewko'

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.blankPage = OnBlankPage(self.driver)

    def test_google_page_redirects_to_encrypted_version_of_itself(self):
        self.blankPage\
            .goToGoogle()\
            .assertOnEncryptedSite()

    def test_google_contains_search_bar(self):
        self.blankPage\
            .goToGoogle()\
            .checkForSearchBar()

    def test_google_search(self):
        self.blankPage\
            .goToGoogle()\
            .inputTextInSearchBar("eminem")\
            .checkPageTitle("eminem")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()