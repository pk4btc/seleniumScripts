# C:\Users\live4\Desktop\My projects\selScripts

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest




class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.nopcommerce.com/")
        self.assertIn("nopCommerce - ASP.NET Open-source Ecommerce Shopping Cart Solution", driver.title)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
