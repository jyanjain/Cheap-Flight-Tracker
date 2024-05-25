import requests

SHEETY_ENDPOINT = "https://api.sheety.co/13318cf8cddcec1ba147a11beded8f5e/flightDeals/users"
BEARER = "jyanjain123123"

def post_new_rows(first_name, last_name, email1):

    body={
        "user":{
            "First Name":first_name,
            "Last Name":last_name,
            "Email":email1,
        }
    }

    headers = {
        "Authorization": f"Bearer {BEARER}",
        "Content-Type": "application/json",
    }
    response = requests.post(url=SHEETY_ENDPOINT, json=body, headers=headers)
    response.raise_for_status()
    print(response.json())