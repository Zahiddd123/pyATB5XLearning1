import allure
import pytest
import requests
from urllib3 import request


@allure.title("Verify the the GET Request of Restful Booker ")
@allure.description("This is the TC to check booking 1 and verify the response")
@pytest.mark.positive
def test_get_request_positive():
    URL= "https://restful-booker.herokuapp.com/booking/1 "
    response_data= requests.get(url=URL)
    print(response_data.text) #to print the response data add -s with the
                              # "pytest filepath --alluredir=allure_results -s"
    assert response_data.status_code == 200

@allure.title("Verify the the GET Request of Restful Booker with invalid booking id ")
@allure.description("This is the TC to check booking -1 and verify the response")
@pytest.mark.positive
def test_get_request_positive():
    URL= "https://restful-booker.herokuapp.com/booking/-1 "
    response_data= requests.get(url=URL)
    print(response_data.text) #to print the response data add -s with the
                              # "pytest filepath --alluredir=allure_results -s"
    assert response_data.status_code == 404
