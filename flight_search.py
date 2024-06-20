import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN_ENDPOINT = 'https://test.api.amadeus.com/v1/security/oauth2/token'
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_SEARCH = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:
    def __init__(self):
        self._api_key = os.environ["Amadeus_API_KEY"]
        self._api_secret = os.environ["Amadeus_API_Secret"]
        self._token = self._get_new_token()

    def _get_new_token(self):
        header = {
            'Content-Type':'application/x-www-form-urlencoded'
        }

        body = {
            "grant_type" : 'client_credentials',
            "client_id" : self._api_key,
            "client_secret" : self._api_secret,
        }

        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)

        print(response.json()['access_token'])
    
        print(f"Access token expries in {response.json()['expires_in']}")

        return response.json()['access_token']

    def get_destination_code(self, city_name):
        headers = {
            "authorization" : f"Bearer {self._token}"
        }

        query = {
            "keyword" : city_name,
            "max" : 2,
            "include" : "AIRPORTS"
        }
        
        response = requests.get(url=IATA_ENDPOINT, headers=headers, params=query)

        print(response.json())

        try:
            code = response.json()["data"][0]['iataCode']

        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
    
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return code
    
    def check_flights(self, origin, destination, from_time, to_time):
        query = {
            "originLocationCode" : origin,
            "destinationLocationCode" : destination,
            "departureDate" : from_time.strftime("%Y-%m-%d"),
            "returnDate" : to_time.strftime("%Y-%m-%d"),
            "adults" : 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }

        headers = {
            "authorization" : f"Bearer {self._token}"
        }

        response = requests.get(url=FLIGHT_SEARCH, headers=headers, params=query)

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()


