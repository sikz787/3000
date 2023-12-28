import requests
import pytest


def test_create2():
    print("create booking TC")
    url = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json = {
        "firstname": str,
        "lastname": str,
        "totalprice": int,
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
    assert data["booking"]["firstname"] == str, "correct name displayed"

