import pytest
import allure
import requests

# pip install pytest allure requests--> install all at once
@allure.title("TC #1 Verify that 2-2=0")
@allure.description("This is smoke TC which check- verify that 2-2=0 ")
@pytest.mark.smoke # Use this mark name to run the specific marked testcase "pytest -m "smoke" file path"
def test_basic_math1():
    assert 2-2==0

@allure.title("TC #2 Verify that 3-3=0")
@allure.description("This is smoke TC which check- verify that 3-3=0 ")
@pytest.mark.skip(reason="Not in used TC")
def test_basic_math2():
    assert 3-3!=0

@allure.title("TC #3 Verify that 1-1=0")
@allure.description("This is smoke TC which check- verify that 1-1=0 ")
@pytest.mark.smoke
def test_basic_math3():
    assert 1-1==0

