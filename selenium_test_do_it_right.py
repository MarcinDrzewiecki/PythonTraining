__author__ = 'drzewko'

import time
from selenium.webdriver.common.keys import Keys

class OnBlankPage(object):
    def __init__(self, driver):
        self.driver = driver

    def goToGoogle(self):
        self.driver.get("http://www.google.com")
        return OnGooglePage(self.driver)

class OnGooglePage(object):
    def __init__(self, driver):
        self.driver = driver

    def assertOnEncryptedSite(self):
        self.driver.assertIn("https://", self.driver.current_url)
        return self

    def checkForSearchBar(self):
        self.driver.find_element_by_xpath("//input[@name='btnK']")
        return self

    def inputTextInSearchBar(self,string):
        inputElement = self.driver.find_element_by_id("lst-ib")
        inputElement.send_keys(string)
        inputElement.send_keys(Keys.ENTER)
        time.sleep(5)
        return self

    def checkPageTitle(self,string):
        assert string in self.driver.title
        return self


