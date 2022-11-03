from models.booking import Booking

import datetime

booking1 = Booking(datetime.date(2022, 11, 4), datetime.time(12, 00), "Metallica", 4, "Studio One", "Music writing session")
booking2 = Booking(datetime.date(2022, 11, 5), datetime.time(11, 00), "Sigur Ros", 3, "Studio Two", "Album recording session")

bookings = [booking1, booking2]

def add_new_booking(booking):
    bookings.append(booking)