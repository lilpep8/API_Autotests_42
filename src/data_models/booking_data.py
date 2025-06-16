from pydantic import BaseModel
from typing import Optional
from src.utils.data_generator import DataGenerator


class BookingDates(BaseModel):
    checkin: str
    checkout: str


class BookingModel(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: Optional[str] = None


# Отдельная модель для дат в методе PATCH
class PatchedBookingDates(BaseModel):
    checkin: Optional[str]
    checkout: Optional[str]


# Отдельная модель для метода PATCH
class PatchedBookingModel(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    totalprice: Optional[int] = None
    depositpaid: Optional[bool] = None
    bookingdates: Optional[PatchedBookingDates] = None
    additionalneeds: Optional[str] = None


class BookingData:

    @staticmethod
    def create_booking_data() -> BookingModel:
        return BookingModel(
            firstname=DataGenerator.generate_first_name(),
            lastname=DataGenerator.generate_last_name(),
            totalprice=DataGenerator.generate_random_int(100, 10000),
            depositpaid=True,
            bookingdates=BookingDates(
                checkin=DataGenerator.generate_random_checkin_date(),
                checkout=DataGenerator.generate_random_checkout_date()
            ),
            additionalneeds=DataGenerator.generate_first_name(),
        )

    @staticmethod
    def patch_booking_data_fullname() -> PatchedBookingModel:
        return PatchedBookingModel(
            firstname=DataGenerator.generate_first_name(),
            lastname=DataGenerator.generate_last_name()
        )


    @staticmethod
    def patch_booking_other_data() -> PatchedBookingModel:
        return PatchedBookingModel(
            totalprice=DataGenerator.generate_random_int(100, 10000),
            bookingdates=PatchedBookingDates(
                checkin=DataGenerator.generate_random_checkin_date(),
                checkout=DataGenerator.generate_random_checkout_date()
            ),
                additionalneeds=DataGenerator.generate_first_name()
        )