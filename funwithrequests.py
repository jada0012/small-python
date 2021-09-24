import requests
from requests import api

api_url = "https://mars-photos.herokuapp.com/"
response = requests.get(api_url).json()
print(response)