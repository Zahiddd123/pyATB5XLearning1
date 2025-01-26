from http.client import responses

import pytest
import allure
import requests

from Nov.ex_09112024_Literals_Variables.Lab017_Strings import first_name


# pip install pytest allure requests--> install all at once
@allure.title("TC#1- Create token")
@allure.description("Verify the create token")
@pytest.mark.create_token
def test_create_token():
    base_url="https://restful-booker.herokuapp.com"
    base_path="/auth"
    url=base_url+base_path

    payload= {"username" : "admin",
    "password" : "password123"}
    headers={"content-type": "application/json"}

    response_data= requests.post(url=url,headers=headers,json=payload)
    assert response_data.status_code == 200

    response_data_token=response_data.json()
    token= response_data_token["token"]
    print(token)
    assert type(token) == str
    assert len(token) == 15
