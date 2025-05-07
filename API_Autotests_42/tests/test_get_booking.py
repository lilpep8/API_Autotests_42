from constants import BASE_URL

# for testing get(without id). get all bookings and check inside
class TestGet:
    def test_get_booking_without_id(self, auth_session):
        # get all bookings
        get_bookings = auth_session.get(f"{BASE_URL}/booking")# method get
        assert get_bookings.status_code == 200

        # create and check booking json
        bookings_data_response = get_bookings.json()
        assert isinstance(bookings_data_response, list), "В ответ не список"
        assert len(bookings_data_response) > 0, "Вернулся пустой список"

        # check everyone booking creation
        for booking in bookings_data_response:
            assert "bookingid" in booking, "Id бронирования не получен"
            assert isinstance(booking["bookingid"], int), "ID бронирования должно быть число"
