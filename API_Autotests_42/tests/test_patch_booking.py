from constants import BASE_URL

# for testing patch. before use post - after use patch
class TestPatch:
    def test_patch_fullname_booking(self, booking_data, patch_booking_data_fullname, auth_session):
        # create booking
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)# method post
        assert create_booking.status_code == 200
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "ID букинга не найден в ответе"

        # check successful creating
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200

        # update booking
        patch_booking = auth_session.patch(f"{BASE_URL}/booking/{booking_id}", json=patch_booking_data_fullname)# method patch
        assert patch_booking.status_code == 200

        # check updated data
        get_updated_data = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_updated_data.status_code == 200

        # make jsons from updated booking and old booking
        booking_data_response = get_booking.json()
        updated_data_response = get_updated_data.json()

        # check updated data
        assert booking_data_response['firstname'] != updated_data_response['firstname'],"Имя не изменилось"
        assert booking_data_response['lastname'] != updated_data_response['lastname'],"Фамилия не изменилась"

        # verify that non-updated fields remain unchanged
        assert booking_data_response['totalprice'] == updated_data_response['totalprice'],"Цена изменилась"
        assert booking_data_response['depositpaid'] == updated_data_response['depositpaid'],"Статус депозита изменился"
        assert booking_data_response['bookingdates']['checkin'] == updated_data_response['bookingdates']['checkin'],"Дата заезда изменилась"
        assert booking_data_response['bookingdates']['checkout'] == updated_data_response['bookingdates']['checkout'],"Дата выезда изменилась"

        # delete session
        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"

        # test successful deletion
        get_deleted_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_deleted_booking.status_code == 404, "Букинг не был удален"


    def test_patch_other_data_booking(self, booking_data, patch_booking_other_data, auth_session):
        # create booking
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)# method post
        assert create_booking.status_code == 200
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "ID букинга не найден в ответе"

        # check successful creating
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200

        # update booking
        patch_booking = auth_session.patch(f"{BASE_URL}/booking/{booking_id}", json=patch_booking_other_data)# method patch
        assert patch_booking.status_code == 200

        # check updated data
        get_updated_data = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_updated_data.status_code == 200

        # make jsons from updated booking and old booking
        booking_data_response = get_booking.json()
        updated_data_response = get_updated_data.json()

        # check updated data
        assert booking_data_response['totalprice'] != updated_data_response['totalprice'],"Цена не изменилась"
        assert booking_data_response['depositpaid'] == updated_data_response['depositpaid'],"Статус депозита не изменился"
        assert booking_data_response['bookingdates']['checkin'] != updated_data_response['bookingdates']['checkin'],"Дата заезда не изменилась"
        assert booking_data_response['bookingdates']['checkout'] != updated_data_response['bookingdates']['checkout'],"Дата выезда не изменилась"

        # verify that non-updated fields remain unchanged
        assert booking_data_response['firstname'] == updated_data_response['firstname'],"Имя не изменилось"
        assert booking_data_response['lastname'] == updated_data_response['lastname'],"Фамилия не изменилась"

        # delete session
        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"

        # test successful deletion
        get_deleted_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_deleted_booking.status_code == 404, "Букинг не был удален"