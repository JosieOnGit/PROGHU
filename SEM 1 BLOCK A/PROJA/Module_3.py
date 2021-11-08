import tweepy
import random
import requests
from tkinter import *
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def refresh():
    print(f"Picked some random Tweets!")
    text1Label["text"] = random.choice(tweetsLst)
    text2Label["text"] = random.choice(tweetsLst)
    root.after(5000, refresh)


tweets = api.user_timeline(screen_name="TowaVEVO",
                           count=200,
                           include_rts=False,
                           exclude_replies=True,
                           tweet_mode="extended",
                           )
tweetsLst = []
for info in tweets:
    tweetsLst.append(info.full_text)

urlLoc = "https://ipapi.co/json"
responseLoc = requests.get(urlLoc)
city = responseLoc.json()["city"]

urlWeather = f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID=67ce6bcc59cc08bbd5cebb9e9bfabc11"
responseWeather = requests.get(urlWeather)
currentTemp = round(responseWeather.json()["main"]["temp"] - 273.15)
currentFeelsLike = round(responseWeather.json()["main"]["feels_like"] - 273.15)
weatherLike = responseWeather.json()["weather"][0]["description"]

root = Tk()
root.title("water mark")
root.geometry("900x480")
root.config(bg="#FFAC00")

mainLabel = Label(master=root, bg="#FFAC00", fg="Black", text="NS Twitter feed", font=("Sans", 30),
                  height=1, width=100)
mainLabel.pack()

subLabel = Label(master=root, bg="#FFAC00", fg="Black", text="Some submitted messages:", font=("Sans", 15),
                 height=2, width=100)
subLabel.pack()

text1Label = Label(master=root, bg="#009CDE", text=random.choice(tweetsLst), font=("Sans", 15),
                   height=4, width=100, wraplength=800)
text1Label.pack()

text2Label = Label(master=root, bg="#009CDE", text=random.choice(tweetsLst), font=("Sans", 15),
                   height=4, width=100, wraplength=800)
text2Label.pack()

currentTempLabel = Label(master=root, bg="#FFAC00",
                         text=f"Current temperature in {city}: {round(currentTemp)}°C",
                         font=("Sans", 10), height=2, width=100)
currentTempLabel.pack()

currentFeelsLikeLabel = Label(master=root, bg="#FFAC00",
                              text=f"Feels like: {currentFeelsLike}°C",
                              font=("Sans", 10), height=2, width=100)
currentFeelsLikeLabel.pack()

currentWeatherLabel = Label(master=root, bg="#FFAC00",
                            text=f"There's currently {weatherLike}",
                            font=("Sans", 10), height=2, width=100)
currentWeatherLabel.pack()

refresh()
root.mainloop()
