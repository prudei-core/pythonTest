from jsonschema import validate

from src.enums.global_enums import GlobalErrorMessages


class ResponseAssert:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate_schema(self, schema):
        validate(self.response_json, schema)

    def validate_pydantic_schema(self, schema):
        schema.parse_obj(self.response_json)

    def assert_status_code(self):
        assert self.response_status == 200, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value
        return self
