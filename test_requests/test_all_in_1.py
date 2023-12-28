import requests
import pytest


# I have changed it from test TC to return_token as a method so that we can use this in PUT which need url,token and booking ID
def create_token():
    url_auth = "https://restful-booker.herokuapp.com/auth"
    headers1 = {"Content-Type": "application/json"}
    json1 = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url_auth, headers=headers1, json=json1)
    data = response.json()
    token = (data["token"])
    print(token)
    return token


def create():
    print("create booking TC")
    url = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
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
    response = requests.post(url=url, headers=headers, json=json)
    assert response.status_code == 200

    data = response.json()
    # to keep id/booking id separate to use it in other methods
    booking_id = data["bookingid"]
    print(booking_id)
    return booking_id
    assert data["booking"]["firstname"] == "sik", "correct name displayed"


# put request we need url which includes booking id, headers with authorisation, id to make changes and also json payload data

def test_put():
    url = "https://restful-booker.herokuapp.com/booking"
    booking_id = create()
    PUT_URL = url + "/" + str(booking_id)
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
    # assert data["booking_id"] is not None  - not needed in Put request
    assert data["firstname"] == "sik", "correct name"
    print(data)


def test_delete():
    url = "https://restful-booker.herokuapp.com/booking"
    booking_id = create()
    PUT_URL = url + "/" + str(booking_id)
    cookie_value = "token=" + create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie_value
    }

    print(headers)

    response = requests.delete(url=PUT_URL, headers=headers)
    assert response.status_code == 201
