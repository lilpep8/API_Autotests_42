from src.api_clients.api_clietns import BookingApi
from src.utils.response_validator import validate_response
from src.data_models.booking_data import BookingResponse, PatchedBookingResponse


class BookingScenarios:
    def __init__(self, api_client: BookingApi): # Типизация для ясности
        self.api_client = api_client


    def create_put_delete_booking(self, booking_data, updated_booking_data):
        """
        Сценарий: создать букинг, провалидировать данные и схему,
        отредактировать его поля, провалидировать данные и схему,
        и удалить букинг.
        Возвращает ID отредактированного и удаленного букига.
        """
        created_booking_data = self.api_client.create_booking(booking_data).json()
        booking_id = created_booking_data.get("bookingid")
        assert booking_id is not None, f"ID не найден в ответе на создание: {created_booking_data}"

        get_booking_data = self.api_client.get_booking(booking_id)
        validate_response(
            get_booking_data,
            model=BookingResponse,
            expected_data=booking_data.model_dump()
        )

        # PUT
        self.api_client.update_booking(booking_id, updated_booking_data)
        get_edited_booking_data = self.api_client.get_booking(booking_id)
        validate_response(
            get_edited_booking_data,
            model=BookingResponse,
            expected_data=updated_booking_data.model_dump()
        )

        self.api_client.delete_booking(booking_id)
        print(f"Букинг с ID {booking_id} успешно создан, отредактирован и удален.")
        return booking_id


    def create_patch_fullname_delete_booking(self, booking_data, updated_booking_data):
        """
        Сценарий: создать букинг, провалидировать данные и схему,
        отредактировать фамилию и имя, провалидировать данные и схему,
        и еудалить букинг.
        Возвращает ID отредактированного и удаленного букига.
        """
        created_booking_data = self.api_client.create_booking(booking_data).json()
        booking_id = created_booking_data.get("bookingid")
        assert booking_id is not None, f"ID не найден в ответе на создание: {created_booking_data}"

        get_booking_data = self.api_client.get_booking(booking_id)
        validate_response(
            get_booking_data,
            model=BookingResponse,
            expected_data=booking_data.model_dump()
        )
        # PATCH
        self.api_client.patch_booking(booking_id, updated_booking_data)
        get_edited_booking_data = self.api_client.get_booking(booking_id)
        validate_response(
            get_edited_booking_data,
            model=PatchedBookingResponse,
            expected_data=updated_booking_data.model_dump()
        )

        self.api_client.delete_booking(booking_id)
        print(f"Букинг с ID {booking_id} успешно создан,"
              f" отредактированы поля first_name, last_name и после был удален.")
        return booking_id


    def create_patch_other_data_delete_booking(self, booking_data, updated_booking_data):
        """
        Сценарий: создать букинг, провалидировать данные и схему,
        отредактировать цену, даты, доп.услуги и провалидировать данные и схему,
        и удалить букинг.
        Возвращает ID отредактированного и удаленного букига.
        """
        created_booking_data = self.api_client.create_booking(booking_data).json()
        booking_id = created_booking_data.get("bookingid")

        assert booking_id is not None, f"ID не найден в ответе на создание: {created_booking_data}"

        get_booking_data = self.api_client.get_booking(booking_id)
        validate_response(
            get_booking_data,
            model=BookingResponse,
            expected_data=booking_data.model_dump()
        )
        # PATCH
        self.api_client.patch_booking(booking_id, updated_booking_data)
        get_edited_booking_data = self.api_client.get_booking(booking_id)
        validate_response(
            get_edited_booking_data,
            model=PatchedBookingResponse,
            expected_data=updated_booking_data.model_dump()
        )

        self.api_client.delete_booking(booking_id)
        print(f"Букинг с ID {booking_id} успешно создан,"
              f" отредактированы поля totalprice, bookingdates(checkin)(checkout),"
              f" additionalneeds и после был удален.")
        return booking_id


    def get_all_bookings(self):
        """
        Сценарий: получить список всех букингов и проверить, что он не пуст
        Возвращает список букингов
        """
        response = self.api_client.get_bookings()
        list_of_bookings = response.json()
        assert len(list_of_bookings) > 0, "Список bookings пуст"

        print(f"Получено {len(list_of_bookings)} букингов.")
        return list_of_bookings
