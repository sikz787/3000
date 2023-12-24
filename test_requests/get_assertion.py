# verify or validate with expected and actual output
import requests


def main():
    my_get = requests.get(
        "https://restful-booker.herokuapp.com/booking/9")  # this can also be written as id = 9 and then url
    assert my_get.status_code == 200
    print(my_get.text)
    print(my_get.status_code)

    data = my_get.json()
    # Assertions, use title which is in data like firstname and so on,this is verification of keys
    assert 'firstname' in data, "any message to verify say - data present"  # firstname is the response data , it can be channels number as well
    assert 'lastname' in data, "any message to verify say - data present"

    # this is verification of data
    assert data["firstname"] == "Mary", "firstname is Mary"
    assert data["lastname"] == "Wilson", "lastname is Wilson"


if __name__ == '__main__':
    main()
