import pytest
from selenium import webdriver
from pickle import TRUE
from sauce_project import swag_labs
def test_add_to_cart():
    driver=webdriver.Firefox()
    url="https://www.saucedemo.com/"
    driver.get(url)
    driver.maximize_window()
    assert TRUE
    pytest