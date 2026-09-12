"""
Covers TC-11 and TC-12 from test_cases.md
API testing example against the public reqres.in test API — demonstrates
API testing concepts (status codes, response body assertions) without Selenium.
"""
import pytest
import requests

BASE_URL = "https://reqres.in/api"


@pytest.mark.regression
def test_get_existing_user_returns_200():
    """TC-11: Fetching a known user ID should return 200 and the correct id in the body."""
    response = requests.get(f"{BASE_URL}/users/2")

    assert response.status_code == 200
    body = response.json()
    assert body["data"]["id"] == 2


def test_get_nonexistent_user_returns_404():
    """TC-12: Fetching a user ID that doesn't exist should return 404."""
    response = requests.get(f"{BASE_URL}/users/9999")

    assert response.status_code == 404
