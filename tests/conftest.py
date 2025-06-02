import pytest
from faker import Faker
import requests
from src.data_models.booking_data import (BookingResponse, BookingDates,
                                          PatchedBookingResponse, PatchedBookingDates)


from src.config.constants import api_config

faker = Faker()


@pytest.fixture(scope="session")
def auth_session():
    session = requests.Session()
    session.headers.update(api_config.HEADERS)

    auth_response = requests.post(
        f"{api_config.BASE_URL}/auth",
        headers=api_config.HEADERS,
        json={"username": "admin", "password": "password123"}
    )

    assert auth_response.status_code == 200, "Ошибка авторизации, статус код не 200"
    token = auth_response.json().get("token")
    assert token is not None, "Токен не найден в ответе"

    session.headers.update({"Cookie": f"token={token}"})
    return session


@pytest.fixture()
def booking_data() -> BookingResponse:
    return BookingResponse(
        firstname=faker.first_name(),
        lastname=faker.last_name(),
        totalprice=faker.random_int(min=100, max=10000),
        depositpaid=True,
        bookingdates=BookingDates(
            checkin="2018-01-01",
            checkout="2019-01-01"
        ),
        additionalneeds="Breakfast"
    )


@pytest.fixture()
def updated_booking_data() -> BookingResponse:
    return BookingResponse(
        firstname=faker.first_name(),
        lastname=faker.last_name(),
        totalprice=faker.random_int(min=100, max=10000),
        depositpaid=True,
        bookingdates=BookingDates(
            checkin="2019-01-01",
            checkout="2020-01-01"
        ),
        additionalneeds="Cigars"
    )


@pytest.fixture()
def patch_booking_data_fullname() -> PatchedBookingResponse:
    return PatchedBookingResponse(
    firstname=faker.first_name(),
    lastname=faker.last_name()
    )


@pytest.fixture()
def patch_booking_other_data() -> PatchedBookingResponse:
    return PatchedBookingResponse(
    totalprice=faker.random_int(min=100, max=10000),
    bookingdates=PatchedBookingDates(
        checkin="2015-01-01",
        checkout="2016-02-03"
    ),
        additionalneeds="Towels"
    )
