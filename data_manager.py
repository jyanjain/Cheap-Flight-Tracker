import requests

SHEETY_ENDPOINT = "https://api.sheety.co/13318cf8cddcec1ba147a11beded8f5e/flightDeals/prices"

AUTHORIZATION_HEADER = {
    "Authorization": "Bearer jyanjain123123"
}
class DataManager:
    
    def __init__(self):
        self.destination_data = {}
    
    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=AUTHORIZATION_HEADER)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
    

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price":{
                    "iataCode":city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}", 
                json=new_data,
                headers=AUTHORIZATION_HEADER
            )

            # response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data)
            # print(response.text)

        
