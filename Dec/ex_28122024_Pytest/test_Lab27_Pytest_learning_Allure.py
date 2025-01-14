# normal method
import allure
import pytest

@allure.title("Verify that create booking, with valid data is working")
@allure.description("This TC is for the positive check")
@pytest.mark.positive
def test_create_booking_positive():
    print("test1")
    assert 1-1==2


# Pytest method
@allure.title("Verify that create booking, with invalid data is working")
@allure.description("This TC is for the positive check")
@pytest.mark.negative
def test_create_booking_negative1():
    print("test2")
    assert 1+1==2

@allure.title("Verify that create booking, with invalid data is workig")
@allure.description("This TC is for the positive check")
@pytest.mark.negative
def test_create_booking_negative2():
    print("test2")
    assert 1+1==2