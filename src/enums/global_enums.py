from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Expected code is not 200"
    WRONG_ELEMENT_COUNT = "Wrong amount of expected elements"
