import requests
import json 


def jprint(obj):
    text=json.dumps(obj, sort_keys=True, indent=4)
    print(text)
# parameters = {
#     "lat": 40.71,
#     "lon": -74
# }
responde = requests.get("http://api.open-notify.org/astros.json")
jprint(responde.json()['people'])