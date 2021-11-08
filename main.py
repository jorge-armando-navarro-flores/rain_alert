import requests
import os
from twilio.rest import Client

account_sid = "AC6a8b98b237fdd8f7ace0c36f55f9dd47"
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

MY_LAT = 20.735460
MY_LONG = -103.349233
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": "ead5d26ff3891f8f89fe2da6f9e1fba1",
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

hourly_weather = weather_data['hourly'][:12]
# condition_codes = [forecast['weather'][0]['id'] for forecast in hourly_weather]

will_rain = False
for hour_data in hourly_weather:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. remember to bring an umbrella ☂️",
        from_='+14199633924',
        to='+523317603281'
    )

    print(message.status)
    print("Bring an Umbrella")
