# C:\Users\live4\Desktop\My projects\selScripts

from selenium import webdriver
import unittest
import os




class testMainPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()


    def test_chekingForm(self):
        driver = self.driver
        driver.get("https://www.nopcommerce.com/")
        driver.implicitly_wait(3)  # seconds
        formElem2 =driver.find_element_by_class_name("facebook")
        formElem2.click()


    def test_checkingTitle(self):
        driver = self.driver
        driver.implicitly_wait(3)  # seconds
        page=driver.title
        self.assertEqual('',page)
        driver.implicitly_wait(3)  # seconds
        print(driver.title)

    def tearDown(self):

        self.driver.close()



if __name__ == "__main__":
    unittest.main()
