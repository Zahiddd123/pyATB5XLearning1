# pytest.fixture method can reuse by the other test methods or test cases

import pytest

@pytest.fixture()
def create_token():
    return "abc"

@pytest.fixture()
def create_booking_id():
    return 1

def test_put(create_token, create_booking_id):
    print(create_token)
    print(create_booking_id)

def test_update_request(create_token, create_booking_id):
    print("token->",create_token)
    print("booking id",create_booking_id)