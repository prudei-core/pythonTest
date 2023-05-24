import requests

from configuration import SERVICE2_URL
from src.base.responseAssert import ResponseAssert
resp = requests.get(SERVICE2_URL)

# print(resp.json())


def test_getting_user_list():
    response = requests.get(SERVICE2_URL)
    test_object = ResponseAssert(response)
    test_object.assert_status_code()

