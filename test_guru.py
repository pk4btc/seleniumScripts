# C:\Users\live4\Desktop\My projects\selScripts

from selenium import webdriver
from selenium.webdriver.support.ui import Select

import unittest




class testMainPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()


    def test_fillup(self):
        driver = self.driver
        driver.get("http://demo.guru99.com/test/login.html")
        driver.find_element_by_id("email").send_keys("adam@wp.pl")
        driver.find_element_by_id("passwd").send_keys("qwerty")
        driver.find_element_by_id("SubmitLogin").click()


    def test_checkTitle(self):
        driver = self.driver
        driver.implicitly_wait(3)  # seconds
        page = driver.title
        self.assertEqual('',page)
        driver.implicitly_wait(3)  # seconds
        print(driver.title)

    def test_toggled_buttons(self):
        driver=self.driver
        driver.get("http://demo.guru99.com/test/radio.html")
        options = driver.find_elements_by_name('webform')
        for clickk in options:
            if clickk.get_attribute("value") == "Option 2":
                clickk.click()
                print("klikniety")
            else: print("nie kliniety")

            if clickk.get_attribute("value") == "checkbox2":
                clickk.click()
                print("klikniety")
            else: print("nie kliniety")

    def test_select_gender_semanticuicommodules(self):
        driver = self.driver
        driver.get("https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select")
        select= Select(driver.find_element_by_tag_name('select'))
        select.select_by_index('2')







    def tearDown(self):

        self.driver.close()



if __name__ == "__main__":
    unittest.main()
