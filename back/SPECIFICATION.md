# Specification

Expose an endpoint which allows a user to get a quotation for a ride.
This endpoint will be called when the user selects a taxi,
to initiate the reservation, and on each time or duration change,
to give an estimation of the price in real time.

The endpoint takes as parameter:

* the ID of the ride they want a quotation for
* the departure time
* an estimated duration of the journey

The endpoint must block the ride for a fixed duration, 
to ensure the ride will still be available when the user validate the reservation.
(duration of the blockage and unblocking are not handled).

The price of a ride is as follow:

* initial charge of 1.00 EUR
* a charge per duration of the journey, depending on the ride type and the period of the day
    * 1.00 EUR per minute between 8PM and 6AM
    * 1.50 EUR per minute between 4PM and 7PM
    * 0.50 EUR per minute for the rest of the day
    * price is multiplied by 0.9 of an "eco" type ride
    * price is multiplied by 1.2 of an "premium" type ride

For example:
* journey starting at 1PM, for a 30 minutes ride, for a eco ride, should be 14.50 €
* journey starting at 5PM, for a 40 minutes ride, for a standard ride, should be 61 €
* journey starting at 10PM, for a 60 minutes ride, for a premium ride, should be 73 €
