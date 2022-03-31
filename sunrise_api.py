from inspect import Parameter
import requests

Parameter = {
    "lat": 12.971599,
    "lng": 77.594566

}

response = requests.get("https://api.sunrise-sunset.org/json", params=Parameter)
response.raise_for_status()
data = response.json()
print(data["results "])