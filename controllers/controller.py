from flask import render_template, request
from app import app
from models.booking import Booking
from models.booking_list import bookings, add_new_booking
import datetime


@app.route('/bookings')
def booking_func():
    return render_template('index.html', title='Home', bookings=bookings)

@app.route('/bookings', methods=['POST'])
def add_booking():
    booking_name = request.form['Band Name']
    location = request.form['Location']
    booking_date = request.form['booking date']
    booking_time = request.form['booking time']
    num_guests = request.form['Num_Guests']
    booking_description = request.form['description']
    new_booking = Booking(booking_date, booking_time, booking_name, num_guests, location, booking_description)
    add_new_booking(new_booking)
    return render_template('index.html', title='Home', bookings=bookings)
