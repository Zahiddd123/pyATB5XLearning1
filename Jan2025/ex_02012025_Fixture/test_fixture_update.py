import pytest
import requests
from dotenv import load_dotenv
import os

from Nov.ex_19112024_Functions.Lab048_Function_input import user_name


# Fixture= Using fixture we can make some common functions and use it in other class or functions,
#          or run it with pytest funtions

@pytest.fixture()
def create_token():                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    create_token():
    load_dotenv()    #use to load the env file
    username= os.getenv("USERNAME")
    password= os.getenv("PASSWORD")
    print(username, password)
#     print("Creating token")
#     url="https://restful-booker.herokuapp.com/auth"
#     payload= {"username" : username,
#     "password" : password}
#     headers={"content-type": "application/json"}
#
#     response_data= requests.post(url=url,headers=headers,json=payload)
#     assert response_data.status_code == 200
#
#     response_data_token=response_data.json()
#     token= response_data_token["token"]
#     print(token)
#
# @pytest.fixture()
# def create_bookingid():
#      pass