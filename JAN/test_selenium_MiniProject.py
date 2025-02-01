from selenium import webdriver
import pytest
import allure
import time

@allure.title("Verify the title and current Url")
@pytest.mark.miniproject
def test_title_current_url():
    driver=webdriver.Edge()
    driver.get("https://demo.us.espocrm.com/")
    print(driver.title)
    CurrentUrl= driver.current_url
    # print(CurrentUrl)
    assert CurrentUrl == "https://demo.us.espocrm.com/"