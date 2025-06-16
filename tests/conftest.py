import pytest
import requests
from src.data_models.booking_data import BookingData


from src.config.constants import api_config


@pytest.fixture(scope="session")
def auth_session():
    session = requests.Session()
        # session.headers.update(api_config.HEADERS)

    auth_response = requests.post(
        f"{api_config.BASE_URL}/auth",
        headers=api_config.HEADERS,
        json=api_config.AUTH_DATA
    )

    assert auth_response.status_code == 200, "Ошибка авторизации, статус код не 200"
    token = auth_response.json().get("token")
    assert token is not None, "Токен не найден в ответе"

    session.headers.update({"Cookie": f"token={token}"})
    return session


@pytest.fixture()
def booking_data():
    return BookingData.create_booking_data()


@pytest.fixture()
def updated_booking_data():
    return BookingData.create_booking_data()


@pytest.fixture()
def patch_booking_data_fullname():
    return BookingData.patch_booking_data_fullname()


@pytest.fixture()
def patch_booking_other_data():
    return BookingData.patch_booking_other_data()
