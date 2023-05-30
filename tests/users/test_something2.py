import pytest
import requests

from configuration import SERVICE2_URL
from src.base.responseAssert import ResponseAssert

resp = requests.get(SERVICE2_URL)


# print(resp.json())


@pytest.mark.production
def test_getting_user_list(main_fxtr, calculate, before_after):
    response = requests.get(SERVICE2_URL)
    test_object = ResponseAssert(response)
    test_object.assert_status_code()
    print(calculate(1, 2))
    print(before_after)


@pytest.mark.skip("Because")
def test_ignore():
    print("This test should be ignored!")
    assert 1 == 1

@pytest.mark.development
@pytest.mark.parametrize("first_parameter, second_parameter, result", [
    (1, 2, 3),
    (-2, 4, 2)
])
def test_calculation(first_parameter, second_parameter, result, calculate):
    assert calculate(first_parameter, second_parameter) == result
