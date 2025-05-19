from .constants import BASE_URL


class TestPatch:
    """Тесты для PATCH-запросов обновления бронирований"""

    def test_patch_fullname_booking(self, booking_data, patch_booking_data_fullname, auth_session):
        """
        PATCH-запросы бронирований.

        Проверяет:
        - Изменяются ли указанные поля (Имя, Фамилия).
        - Остаются прежними поля, которые не были указаны.
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

        # Update booking
        patch_booking = auth_session.patch(
            f"{BASE_URL}/booking/{booking_id}",
            json=patch_booking_data_fullname
        )
        assert patch_booking.status_code == 200, "Не удалось обновить бронирование"

        # Check updated data
        get_updated_data = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_updated_data.status_code == 200, "Не удалось получить обновленные данные"

        # Make jsons from responses
        booking_data_response = get_booking.json()
        updated_data_response = get_updated_data.json()

        # Check updated fields
        assert booking_data_response['firstname'] != updated_data_response['firstname'],\
            "Имя не изменилось"

        assert booking_data_response['lastname'] != updated_data_response['lastname'],\
            "Фамилия не изменилась"

        # Verify unchanged fields
        assert booking_data_response['totalprice'] == updated_data_response['totalprice'],\
            "Цена изменилась"

        assert booking_data_response['depositpaid'] == updated_data_response['depositpaid'],\
            "Статус депозита изменился"

        assert booking_data_response['bookingdates']['checkin'] == updated_data_response['bookingdates']['checkin'],\
            "Дата заезда изменилась"

        assert booking_data_response['bookingdates']['checkout'] == updated_data_response['bookingdates']['checkout'],\
            "Дата выезда изменилась"

        # Cleanup - delete booking
        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201,\
            f"Ошибка при удалении бронирования с ID {booking_id}"

        # Verify deletion
        get_deleted_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_deleted_booking.status_code == 404, "Бронирование не было удалено"


    def test_patch_other_data_booking(self, booking_data, patch_booking_other_data, auth_session):
        """
        PATCH-запросы бронирований.

        Проверяет:
        - Изменяются ли указанные поля (Цена, дата, дополнительные услуги)
        - Остаются прежними поля, которые не были указаны(Имя, Фамилия)
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

        # Update booking
        patch_booking = auth_session.patch(
            f"{BASE_URL}/booking/{booking_id}",
            json=patch_booking_other_data
        )   # Method patch
        assert patch_booking.status_code == 200, "Не удалось обновить бронирование"

        # Check updated data
        get_updated_data = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_updated_data.status_code == 200, "Не удалось получить обновленные данные"

        # Make jsons from responses
        booking_data_response = get_booking.json()
        updated_data_response = get_updated_data.json()

        # Check updated fields
        assert booking_data_response['totalprice'] != updated_data_response['totalprice'],\
            "Цена не изменилась"

        assert booking_data_response['depositpaid'] == updated_data_response['depositpaid'],\
            "Статус депозита не изменился"

        assert booking_data_response['bookingdates']['checkin'] != updated_data_response['bookingdates']['checkin'],\
            "Дата заезда не изменилась"

        assert booking_data_response['bookingdates']['checkout'] != updated_data_response['bookingdates']['checkout'],\
            "Дата выезда не изменилась"

        # Verify unchanged fields
        assert booking_data_response['firstname'] == updated_data_response['firstname'],\
            "Имя не изменилось"

        assert booking_data_response['lastname'] == updated_data_response['lastname'],\
            "Фамилия не изменилась"

        # Cleanup - delete booking
        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201,\
            f"Ошибка при удалении бронирования с ID {booking_id}"

        # Verify deletion
        get_deleted_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_deleted_booking.status_code == 404, "Бронирование не было удалено"
