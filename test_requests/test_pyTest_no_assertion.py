# instead of assertion we have pytest library we can use, best practice,pytest files should start from test_
# no main function, create normal function by test_ and name of the function so that pytest can recognise

import pytest
import requests


def test_1():
    assert 4 == 4


def test_2():
    assert 5 == 5


def test_get_url():
    my_get = requests.get(
        "https://restful-booker.herokuapp.com/booking/1685")  # this can also be written as id = 9 and then url
    assert my_get.status_code == 200
    print(my_get.text)
    print(my_get.status_code)

    data = my_get.json()

    # Assertions, use title which is in data like firstname and so on,this is verification of keys
    assert 'firstname' in data, "any message to verify say - data present"  # firstname is the response data , it can be channels number as well
    assert 'lastname' in data, "any message to verify say - data present"

    # this is verification of data
    assert data["firstname"] == "Jim", "firstname is Jim"
    assert data["lastname"] == "Brown", "lastname is Brown"
