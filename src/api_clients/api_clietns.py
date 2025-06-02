from src.config.constants import api_config

class BookingApi:
    def __init__(self, auth_session):
        self.auth_session = auth_session
        self.base_url = api_config.BASE_URL


    def create_booking(self, booking_data):
        """Отправляет запрос на создание букинга."""
        return self.auth_session.post(
            f"{self.base_url}/booking",
            json=booking_data.model_dump()
        )


    def get_bookings(self):
        """Отправляет запрос на получение списка букингов."""
        return self.auth_session.get(f"{api_config.BASE_URL}/booking")


    def get_booking(self, booking_id):
        """Отправляет запрос на получение одного букинга."""
        return self.auth_session.get(f"{self.base_url}/booking/{booking_id}")


    def update_booking(self, booking_id, upd_booking_data):
        """Отправляет запрос на обновление букинга."""
        return self.auth_session.put(
            f"{self.base_url}/booking/{booking_id}",
            json=upd_booking_data.model_dump()
        )


    def patch_booking(self, booking_id, upd_booking_data):
        """Отправляет запрос на обновление указанных полей букинга."""
        return self.auth_session.patch(
            f"{self.base_url}/booking/{booking_id}",
            json=upd_booking_data.model_dump(exclude_none=True)
        )


    def delete_booking(self, booking_id):
        """Отправляет запрос на удаление букинга."""
        return self.auth_session.delete(f"{self.base_url}/booking/{booking_id}")

