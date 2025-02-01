import pytest
import allure
from  selenium import webdriver

@allure.title("Verify the title is as per expected")
@pytest.mark.regression
def test_vwo_login():
    driver= webdriver.Edge()
    driver.get("https://app.vwo.com") #Used to launch the url
    print(driver.title)
    # Pageurl=driver.current_url # Used to fetch the current page url
    # print(Pageurl)
    assert driver.title == "Login - VWO" # Use to fetch the title of the page