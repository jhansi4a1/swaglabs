import time  
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class swag_labs:
    driver=webdriver.Firefox()
    url="https://www.saucedemo.com/"
    driver.get(url)
    driver.maximize_window()
    name=driver.title
    print(name)
    def add_to_cart(self):
        self.driver.find_element(by=By.ID,value="user-name").send_keys("standard_user")
        self.driver.find_element(by=By.ID,value="password").send_keys("secret_sauce")
        self.driver.find_element(by=By.ID,value="login-button").click()
        self.driver.find_element(by=By.XPATH,value="//button[@id='react-burger-menu-btn']").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,value="//button[@id='react-burger-cross-btn']").click()
        filter=self.driver.find_element(by=By.XPATH,value="//select[@class='product_sort_container']")
        drp=Select(filter)
        drp.select_by_value("lohi")
        self.driver.find_element(by=By.XPATH,value="//button[@id='add-to-cart-sauce-labs-bike-light']").click()
        time.sleep(3)
        self.driver.find_element(by=By.ID,value="shopping_cart_container").click()
        self.driver.find_element(by=By.ID,value="checkout").click()
        #name=self.driver.find_element(by=By.ID,value="item_0_title_link")
        #print(name.text)
        #price=self.driver.find_element(by=By.XPATH,value="//div[@class='inventory_item_price']")
        #print(price.text)
        self.driver.find_element(by=By.ID,value="first-name").send_keys("jhansi")
        self.driver.find_element(by=By.ID,value="last-name").send_keys("latha")
        self.driver.find_element(by=By.ID,value="postal-code").send_keys("12345")
        self.driver.find_element(by=By.ID,value="continue").click()
        time.sleep(3)
        self.driver.find_element(by=By.ID,value="finish").click()
        time.sleep(2)
        self.driver.find_element(by=By.ID,value="back-to-products").click()
        
s=swag_labs()
s.add_to_cart()
