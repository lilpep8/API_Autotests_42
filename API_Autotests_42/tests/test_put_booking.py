from constants import BASE_URL

# for testing put. before use post - after use put
class TestPut:
    def test_put_booking(self, booking_data, updated_booking_data, auth_session):
        # create booking
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)# method post
        assert create_booking.status_code == 200
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "ID букинга не найден в ответе"

        # check successful creating
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200

        # update booking
        put_booking = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json=updated_booking_data)# method put
        assert put_booking.status_code == 200

        # check updated data
        get_updated_data = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_updated_data.status_code == 200

        # make jsons from updated booking and old booking
        booking_data_response = get_booking.json()
        updated_data_response = get_updated_data.json()

        # verify that updated fields changed
        assert booking_data_response['firstname'] != updated_data_response['firstname'],"Имя не изменилось"
        assert booking_data_response['lastname'] != updated_data_response['lastname'],"Фамилия не изменилась"
        assert booking_data_response['totalprice'] != updated_data_response['totalprice'],"Цена не изменилась"
        assert booking_data_response['depositpaid'] == updated_data_response['depositpaid'],"Статус депозита не изменился"
        assert booking_data_response['bookingdates']['checkin'] != updated_data_response['bookingdates']['checkin'],"Дата заезда не изменилась"
        assert booking_data_response['bookingdates']['checkout'] != updated_data_response['bookingdates']['checkout'],"Дата выезда не изменилась"

        # delete session
        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"

        # test successful deletion
        get_deleted_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_deleted_booking.status_code == 404, "Букинг не был удален"
