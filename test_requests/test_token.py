import requests
import pytest


# I have changed it from test TC to return_token as a method so that we can use this in PUT which need url,token and booking ID
def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=json)
    data = response.json()
    token = (data["token"])
    print(token)
    return token


# put request we need url which includes booking id, headers with authorisation, id to make changes and also json payload data

def test_put():
    url = "https://restful-booker.herokuapp.com/booking"
    booking_id = "str"
    PUT_URL = url + "/" + booking_id
    cookie_value = "token=" + create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie_value
    }

    print(headers)
    json = {
        "firstname": "sik",
        "lastname": "tyagi",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "super bowls"
    }
    response = requests.put(url=PUT_URL, headers=headers, json=json)
    assert response.status_code == 200
    data = response.json()
    assert data["firstname"] == "sik", "correct name"
    print(data)
