from data_manager import DataManager
from flight_search import FlightSearch
import datetime
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager
import time

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# print(sheet_data)

ORIGIN_IATA_CODE = "LON"

flight_search = FlightSearch()

notification_manager = NotificationManager()

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch

    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_data()

flights = flight_search.check_flights

tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
six_month_from_today = datetime.datetime.now() + datetime.timedelta(days=(6*30))

for destination in sheet_data:
    flights = flight_search.check_flights(
        ORIGIN_IATA_CODE,
        destination['iataCode'],
        tomorrow,
        six_month_from_today
    )

    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']} : {cheapest_flight.price}")
    time.sleep(2)

    if cheapest_flight != "N/A" and float(cheapest_flight.price) < float(destination["lowestPrice"]):
        print(f"Lower price flight found to {destination['city']}!")
        notification_manager.send_email(
            email_body=f"Low price alert! Only {cheapest_flight.price} to fly from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport} on {cheapest_flight.out_date} to {cheapest_flight.return_date}"
        )

