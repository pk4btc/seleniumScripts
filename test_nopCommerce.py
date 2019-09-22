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


    def test_chekingForm(self):
        driver = self.driver
        driver.get("http://demo.guru99.com/test/login.html")
        driver.find_element_by_id("email").send_keys("adam@wp.pl")
        driver.find_element_by_id("passwd").send_keys("qwerty")
        driver.find_element_by_id("SubmitLogin").click()


    def test_checkingTitle(self):
        driver = self.driver
        driver.implicitly_wait(3)  # seconds
        page=driver.title
        self.assertEqual('',page)
        driver.implicitly_wait(3)  # seconds
        print(driver.title)



    def test_if_logo_goback(self):
        driver = self.driver
        driver.get("https://www.nopcommerce.com/shoppingcart.aspx")
        logo = driver.find_element_by_css_selector('div.header-logo a img')
        src_base=logo.tag_name
        logo.click()

        print(f'znalezione za pomoca {src_base}')
        if driver.title == 'nopCommerce - ASP.NET Open-source Ecommerce Shopping Cart Solution':
            print('powrot do home ')

        else:print('fail')

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

    def test_acttionChains_decathlon(self):
        driver = self.driver

        driver.get("https://www.emag.pl")
        time.sleep(2)

        # akcesoria = driver.find_element(By.XPATH,'//a[@href="//laptopy-tablety-i-telefony//d?ref=hdr_menu_department_1"]')


        akcesoria = driver.find_element(By.LINK_TEXT,'Kultura i Rozrywka')
        actions = ActionChains(driver)
        actions.move_to_element(akcesoria).click().perform()


        time.sleep(2)











    def tearDown(self):

        self.driver.close()



if __name__ == "__main__":
    unittest.main()
