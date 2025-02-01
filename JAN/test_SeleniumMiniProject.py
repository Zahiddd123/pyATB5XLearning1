from allure_pytest.utils import allure_title
from selenium import webdriver
import allure
import pytest

@allure.title("Verify the source code contain the text or not")
def test_katalon_text():
    driver=webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    if "CURA Healthcare Service" in driver.page_source:
        print("Text found")
    else:
        print("Text not found on the page")
        pytest.fail("Text not found on the page")