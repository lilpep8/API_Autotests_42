from .constants import BASE_URL


class TestPut:
    """Тесты для PUT-запросов полного обновления бронирований."""

    def test_put_booking(self, booking_data, updated_booking_data, auth_session):
        """
        PUT-запросы бронирований.

        Проверяет:
        - Тестирование полного обновления всех данных бронирования.
        - Проверка корректности всех обновленных полей.
        """
        # Create booking
        create_booking = auth_session.post(
            f"{BASE_URL}/booking",
            json=booking_data
        )   # Method post
        assert create_booking.status_code == 200, "Не удалось создать бронирование"
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "ID бронирования не найден в ответе"

        # Check successful creation
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, "Не удалось получить бронирование"

        # Update booking with PUT
        put_booking = auth_session.put(
            f"{BASE_URL}/booking/{booking_id}",
            json=updated_booking_data
        )   # Method put
        assert put_booking.status_code == 200, "Не удалось обновить бронирование"

        # Check updated data
        get_updated_data = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_updated_data.status_code == 200, "Не удалось получить обновленные данные"

        # Prepare response data for comparison
        booking_data_response = get_booking.json()
        updated_data_response = get_updated_data.json()

        # Verify all fields were updated as expected
        assert booking_data_response['firstname'] != updated_data_response['firstname'],\
            "Имя не изменилось"

        assert booking_data_response['lastname'] != updated_data_response['lastname'],\
            "Фамилия не изменилась"

        assert booking_data_response['totalprice'] != updated_data_response['totalprice'],\
            "Цена не изменилась"

        assert booking_data_response['depositpaid'] == updated_data_response['depositpaid'],\
            "Статус депозита не изменился"

        assert booking_data_response['bookingdates']['checkin'] != updated_data_response['bookingdates']['checkin'],\
            "Дата заезда не изменилась"
        assert booking_data_response['bookingdates']['checkout'] != updated_data_response['bookingdates']['checkout'],\
            "Дата выезда не изменилась"

        # Verify deposit status remains unchanged
        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201,\
            f"Ошибка при удалении бронирования с ID {booking_id}"

        # Cleanup - delete booking
        get_deleted_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_deleted_booking.status_code == 404, "Бронирование не было удалено"
