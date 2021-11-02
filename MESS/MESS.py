import requests

url = "https://ipapi.co/json"
response = requests.get(url)
location = response.json()["city"]
print(location)

