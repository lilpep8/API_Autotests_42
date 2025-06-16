from src.api_clients.api_clietns import BookingApi
from src.scenarios.scenario import BookingScenarios


class TestBookings:
    def test_get_bookings(self, auth_session):
        scenario = BookingScenarios(api_client=BookingApi(auth_session))
        bookings = scenario.get_all_bookings()
        assert bookings is not None


    def test_put_booking(self, auth_session, booking_data, updated_booking_data):
     scenario = BookingScenarios(api_client=BookingApi(auth_session))
     booking_id = scenario.create_put_delete_booking(booking_data, updated_booking_data)
     assert booking_id is not None


    def test_patch_fullname_booking(self, auth_session, booking_data, patch_booking_data_fullname):
        scenario = BookingScenarios(api_client=BookingApi(auth_session))
        booking_id = scenario.create_patch_fullname_delete_booking(booking_data, patch_booking_data_fullname)
        assert booking_id is not None


    def test_patch_other_data_for_booking(self, auth_session, booking_data, patch_booking_other_data):
        scenario = BookingScenarios(api_client=BookingApi(auth_session))
        booking_id = scenario.create_patch_other_data_delete_booking(booking_data, patch_booking_other_data)
        assert booking_id is not None
