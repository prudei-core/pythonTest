import pytest
from jsonschema import validate

from src.base.responseAssert import ResponseAssert
from src.schemas.get import GET_BYBIT_SCHEMA
from src.pydantic_schemas.getbybitpydanticschema import GetByBitPydanticSchema

def test_get_bybit(get_url):
    """
    My first description in the test
    """
    r = ResponseAssert(get_url)
    r.assert_status_code() \
        .validate_schema(GET_BYBIT_SCHEMA)


def test_data_bybit(get_url):
    response_data = get_url.json()
    validate(response_data, GET_BYBIT_SCHEMA)
    # print(response_data.get("retCode"))


def test_new_pydantic_schema(get_url):
    r = ResponseAssert(get_url)
    r.assert_status_code() \
        .validate_pydantic_schema(GetByBitPydanticSchema)
