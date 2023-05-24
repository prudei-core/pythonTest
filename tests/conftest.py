import pytest
import requests

from configuration import SERVICE_URL


@pytest.fixture()
def get_url():
    print("Getting url..")
    return requests.get(SERVICE_URL)
