# get url

import requests


def main():
    my_get = requests.get("https://restful-booker.herokuapp.com/booking/9")
    # to get details from api url
    print(my_get.text)
    print(my_get.status_code)
    print(my_get.headers)
    print(my_get.json())

    # to verify, use assertions instead of if loop
    if my_get.status_code == 200:
        print("Get - pass")
    else:
        print("get - fail")


if __name__ == "__main__":
    main()
