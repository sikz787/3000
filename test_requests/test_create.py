import requests
import pytest


# in create we need url, headers(content type and accept), data(json data body like names and all),body(payload) and we will verify Id and Json information


def test_create():
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

    booking_id=data["bookingid"]
    print(booking_id)
    assert data["bookingid"] is not None
    assert data["booking"]["firstname"] == "sik", "correct name"
