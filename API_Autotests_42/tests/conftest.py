import pytest
from faker import Faker
import requests


from tests.constants import HEADERS, BASE_URL

faker = Faker()


@pytest.fixture(scope="session")
def auth_session():
    session = requests.Session()
    session.headers.update(HEADERS)



    auth_response = requests.post(f"{BASE_URL}/auth",
                             headers=HEADERS,
                             json={"username": "admin", "password": "password123"})

    assert auth_response.status_code == 200, "Ошибка авторизации, статус код не 200"
    token = auth_response.json().get("token")
    assert token is not None, "Токен не найден в ответе"

    session.headers.update({"Cookie": f"token={token}"})
    return session


@pytest.fixture()
def booking_data():
    return {
    "firstname" : faker.first_name(),
    "lastname" : faker.last_name(),
    "totalprice" : faker.random_int(min=100, max=10000),
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}


@pytest.fixture()
def updated_booking_data(booking_data):
    updated = booking_data.copy()
    updated.update({
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=10000),
        "bookingdates": {
            "checkin": "2019-01-01",
            "checkout": "2020-01-01"
        },
        "additionalneeds": "Cigars"
    })
    return updated


@pytest.fixture()
def patch_booking_data_fullname():
    return {
    "firstname" : faker.first_name(),
    "lastname" : faker.last_name()
    }


@pytest.fixture()
def patch_booking_other_data():
    return {
        "totalprice": faker.random_int(min=100, max=10000),
        "bookingdates": {
            "checkin": "2015-01-01",
            "checkout": "2016-01-01"
        },
        "additionalneeds": "Towels"
    }


