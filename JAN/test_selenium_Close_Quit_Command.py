from selenium import webdriver
import pytest
import allure
import time

def test_close_command():
    driver=webdriver.Edge()
    driver.get("https://app.vwo.com")
    time.sleep(5)
    driver.close()

def test_quite_command():
    driver=webdriver.Edge()
    driver.get("https://app.vwo.com")
    time.sleep(5)
    driver.quit()
