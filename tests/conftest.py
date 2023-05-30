import pytest
from random import randrange


@pytest.fixture()
def main_fxtr():
    print("This is main fixture")


def _calculate(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return None


@pytest.fixture()
def calculate():
    return _calculate


@pytest.fixture()
def before_after():
    print("Before test")
    number = randrange(0, 1000)
    yield number
    print(f"number {number}")
    print("After test")
