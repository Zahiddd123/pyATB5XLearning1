from http.client import responses

import pytest
import allure
import requests
from pycparser.ply.yacc import token

from Dec.ex_07122024_Exception.Lab21_Exception_Exampple1 import full_path
from Nov.ex_09112024_Literals_Variables.Lab017_Strings import first_name

base_url="https://restful-booker.herokuapp.com"
headers={"content-type":"application/json"}
# pip install pytest allure requests--> install all at once

def get_token():

    base_path="/auth"
    url=base_url+base_path

    payload= {"username" : "admin",
    "password" : "password123"}


    response_data= requests.post(url=url,headers=headers,json=payload)
    assert response_data.status_code == 200

    response_data_token=response_data.json()
    token= response_data_token["token"]
    print(token)
    assert type(token) == str
    assert len(token) == 15
    return token

def get_booking_id():
    base_path = "/booking"
    full_url = base_url + base_path

    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response_data = requests.post(url=full_url, headers=headers, json=payload)

    # status code verification
    assert response_data.status_code == 200

    # Booking ID >0, FirstName= "Jim" verification
    response_data_json = response_data.json()
    bookingid = response_data_json["bookingid"]
    print(bookingid)
    return bookingid


def test_put_request():
    token = get_token()
    bookingid= get_booking_id()
    print(token)
    print(bookingid)
    base_path= "/booking/"+str(bookingid)
    full_url_path= base_url+base_path
    cookie= "token="+token
    headers={
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    json_payload= {
        "firstname": "Zahid",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response= requests.put(url=full_url_path,headers=headers,json=json_payload)
    assert response.status_code == 200
    assert response.json()["firstname"] == "Zahid"

@pytest.mark.delete
def test_delete_request():
    URL= "https://restful-booker.herokuapp.com/booking/"

    bookingid= get_booking_id()
    full_url = URL + str(bookingid)
    token= get_token()
    cookie= "token="+token
    headers={ "Content-Type": "application/json",
              "Cookie": cookie}
    response= requests.delete(url=full_url,headers=headers)
    assert response.status_code == 201








