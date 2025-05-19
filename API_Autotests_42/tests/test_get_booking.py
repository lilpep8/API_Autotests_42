from .constants import BASE_URL


class TestGet:
    """Тесты для GET-запросов получения бронирований"""

    def test_get_booking_without_id(self, auth_session):
        """
        Тест получения всех бронирований без указания ID.

        Проверяет:
        - Код ответа.
        - Структуру ответа.
        - Наличие и тип ID бронирований.
        """
        # Get all bookings
        get_bookings = auth_session.get(f"{BASE_URL}/booking") # Method get
        assert get_bookings.status_code == 200

        # Create and check booking json
        bookings_data_response = get_bookings.json()
        assert isinstance(bookings_data_response, list), "В ответ не список"
        assert len(bookings_data_response) > 0, "Вернулся пустой список"

        # Check everyone booking creation
        for booking in bookings_data_response:
            assert "bookingid" in booking, "Id бронирования не получен"
            assert isinstance(booking["bookingid"], int), "ID бронирования должно быть число"
