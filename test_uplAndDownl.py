# C:\Users\live4\Desktop\My projects\selScripts

from selenium import webdriver

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


import unittest
from selenium.webdriver import ActionChains

import os




class testMainPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()




    def test_DragDrop(self):
        driver= self.driver
        wait = WebDriverWait(driver, 10)
        driver.get("http://listmoz.com/")
        driver.implicitly_wait(1)  # seconds
        x=1
        while x < 10:
            driver.implicitly_wait(2)  # seconds
            driver.find_element_by_name("add").send_keys(f'Eat {x}')
            driver.find_element_by_id('submit').click()
            x=x+1
        driver.implicitly_wait(2)  # seconds
        WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/ul/li[1]')))
        # time.sleep(3)
        first = driver.find_element_by_xpath('/html/body/div/ul/li[1]')
        put =  driver.find_element_by_xpath('/html/body/div/ul/li[2]')
        put.click()
        action_chains = ActionChains(driver)
        action_chains.drag_and_drop(first,put).perform()
        driver.implicitly_wait(1)  # seconds

    def test_upload(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(chrome_options=chrome_options)

        driver.get('https://www.freepdfconvert.com/pl')

        input_upl = driver.find_element_by_class_name('file-upload-input')
        input_upl.send_keys(os.getcwd(), r"\Untitled.png")

    def test_alert(self):
        driver=self.driver
        alert_popup = Alert(driver)
        driver.get('https://itstillworks.com/put-popup-message-website-8526989.html')
        time.sleep(2)
        alert_popup.dismiss()
        time.sleep(1)

    def test_table(self):
        driver = self.driver
        driver.get('http://demo.guru99.com/test/web-table-element.php')
        company_desired_name = driver.find_element_by_xpath('/html/body/div/div[3]/div[1]/table/tbody/tr[2]/td[1]/a')
        company_desired_name.click()






    def tearDown(self):

        self.driver.close()



if __name__ == "__main__":
    unittest.main()
