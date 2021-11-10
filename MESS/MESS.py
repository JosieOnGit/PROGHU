
import requests

url = "https://ipapi.co/json"
response = requests.get(url)
location = response.json()["city"]
print(location)

urlWeather = f"https://api.openweathermap.org/data/2.5/weather?q={location}&APPID=67ce6bcc59cc08bbd5cebb9e9bfabc11"
responseWeather = requests.get(urlWeather)
currentTemp = responseWeather.json()["main"]["temp"]
weatherLike = responseWeather.json()["weather"][0]["main"]
print(currentTemp)
print(weatherLike)
