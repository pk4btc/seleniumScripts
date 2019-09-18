# C:\Users\live4\Desktop\My projects\selScripts

from selenium import webdriver

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


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










    def tearDown(self):

        self.driver.close()



if __name__ == "__main__":
    unittest.main()
