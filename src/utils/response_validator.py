import pytest
from pydantic import BaseModel, ValidationError
from requests import Response
from typing import Type

from src.data_models.booking_data import PatchedBookingModel


def validate_response(
    response: Response,
    model: Type[BaseModel],
    expected_status: int = 200,
    expected_data: dict | None = None
) -> BaseModel:
    """
    Универсальный валидатор ответа API:
    - Проверка status_code
    - Валидация схемы через Pydantic
    - Сравнение с ожидаемыми данными (опционально)

    :return: объект модели
    """

    data = None
    parsed = None

    if response.status_code != expected_status:
        pytest.fail(f"Expected status {expected_status}, got {response.status_code}: {response.text}")

    try:
        data = response.json()
    except Exception as e:
        pytest.fail(f"Ошибка парсинга JSON: {e}\nResponse: {response.text}")

    try:
        parsed = model(**data)
    except ValidationError as e:
        pytest.fail(f"Pydantic валидация не прошла:\n{e}")

    # Часть валидатора для метода PATCH
    # Проверяет только заданные поля, игнорируя None
    if expected_data:
        if issubclass(model, PatchedBookingModel):
            actual_dict = parsed.model_dump(exclude_unset=True)
            expected_filtered = {k: v for k, v in expected_data.items() if v is not None}

            for key, expected_value in expected_filtered.items():
                actual_value = actual_dict.get(key, None)
                if actual_dict == expected_value:
                    pytest.fail(
                        f"Проверка patch: поле '{key}' не совпадает.\n"
                        f"Expected: {expected_value}\n"
                        f"Actual: {actual_value}"
                    )

    else:
        expected_model = model(**expected_data) # Обернём данные в такую же модель для сравнения
        if parsed.model_dump(exclude_unset=True) != expected_model.model_dump(exclude_unset=True, exclude_none=True):
            pytest.fail(
                f"Данные ответа не совпадают с ожидаемыми:\n"
                f"Expected: {expected_model.model_dump()}\n"
                f"Actual:   {parsed.model_dump()}"
            )

    return parsed
