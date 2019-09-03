# C:\Users\live4\Desktop\My projects\selScripts

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest




class testMainPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()



    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.nopcommerce.com/")

        self.assertIn("nopCommerce - ASP.NET Open-source Ecommerce Shopping Cart Solution", driver.title)


    def tearDown(self):
        self.driver.close()

    def test_chekingForm(self):
        driver = self.driver
        driver.get("https://www.nopcommerce.com/")

        formElem=driver.find_element_by_id("newsletter-email")
        formElem.send_keys("Adas")

        formElem2=driver.find_element_by_name("Email")
        formElem2.send_keys("amen@wp.com")

        formElem3=page.find_element_by_name("Enquiry")
        formElem3.send_keys("Help to recive new  orders from shop")

        formElemSubmit=driver.find_element_by_name("send-email")
        formElemSubmit.submit()












if __name__ == "__main__":
    unittest.main()
