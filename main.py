import requests
import os
from twilio.rest import Client

# Signup For OpenweatherMap at https://openweathermap.org/
ap1_key = "05cbc6ad70c90712a228074827d5ab4d"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall?"

# Signup for a Twilio account at https://www.twilio.com/try-twilio
account_sid = "ACa72adb30e49344644cd1d0b1a24e35ce"
auth_token = "715a2cc7b78e9776d4a602d58bfb9ed9"

# Use your own Longitude and Latitude here
parameters = {
    "lat": 9.058036,# Longitude
    "lon": 7.489061,# Latitude
    "appid": ap1_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=parameters)
data = response.json()

will_rain = False
# Getting the hourly data for 12 hours
weather_condition = data["hourly"][:12]
for hour in weather_condition:
    # checking the weather code to know if it rains
    code = hour["weather"][0]["id"]
    # condition to know if it will rain using the code
    if int(code) < 700:
        will_rain = True

if will_rain:
    # Sending message to user if there will be rain with the next 12 hours
    try:
        client = Client(account_sid, auth_token)
        print("Connecting to server :-) \nConnected.")
        print("Sending Message.......")
        message = client.messages \
            .create(
            body="It's Going to rain Today, Move with an Umbrella(☔).",
            from_='+1 507 618 6371',
            to='+234 814 982 4418',
        )
    except Exception as error:
        print(error)
        print("Failed 😔😔")
    else:
        print("Sent ✅✔")
