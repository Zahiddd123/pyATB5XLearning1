import pytest
import allure
import requests

from Nov.ex_09112024_Literals_Variables.Lab017_Strings import first_name


# pip install pytest allure requests--> install all at once
@allure.title("TC#1- Create booking CRUD Positive")
@allure.description("Verify the create booking")
@pytest.mark.crud
def test_create_booking_positive():
    base_url="https://restful-booker.herokuapp.com"
    base_path="/booking"
    full_url= base_url+base_path
    headers= { "content-type": "application/json"
 }
    payload= {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
    response_data=requests.post(url=full_url,headers=headers,json=payload)

    #status code verification
    assert response_data.status_code == 200

    #Booking ID >0, FirstName= "Jim" verification
    response_data_json= response_data.json()
    bookingid= response_data_json["bookingid"]
    print(bookingid)

    assert bookingid is not None
    assert bookingid > 0
    assert type(bookingid) == int

    firstName= response_data_json["booking"]["firstname"]
    print(firstName)

    assert firstName == "Jim"
    assert type(firstName) == str

    lastname= response_data_json["booking"]["lastname"]
    totalprice= response_data_json["booking"]["totalprice"]
    depositpaid= response_data_json["booking"]["toolpaid"]

    assert lastname == "Brown"
    assert totalprice == "111"
    assert depositpaid == ("True")

    checkin= response_data_json["booking"]["bookingdates"]["checkin"]
    checkout= response_data_json["booking"]["bookingdates"]["checkout"]

    assert checkin == "2018-01-01"
    assert checkout == "2019-01-01"

    time= response_data.elapsed.total_seconds()  #use to verify the time taken
    assert time < 3

@allure.title("TC#2 Create booking CRUD negative")
@allure.description("Verify the create booking using payload null")
@pytest.mark.crud
def test_create_booking_negative_tc2():
        base_url = "https://restful-booker.herokuapp.com"
        base_path = "/booking"
        full_url = base_url + base_path
        headers = {"content-type": "application/json"
                   }
        payload = {}
        response_data = requests.post(url=full_url, headers=headers, json=payload)

        # status code verification
        assert response_data.status_code == 500
        assert response_data.text == "Internal Server Error"
