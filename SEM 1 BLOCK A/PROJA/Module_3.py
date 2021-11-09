
import tweepy
import requests
from tkinter import *
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret,
    weatherKey
)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def getTweets():
    tweets = api.user_timeline(screen_name="TowaVEVO",
                               count=200,
                               since_id="1457647866449645568",
                               include_rts=False,
                               exclude_replies=True,
                               tweet_mode="extended",
                               )
    tweetsLst = []
    for info in tweets:
        tweetsLst.append(f"- {info.full_text}")
    return tweetsLst


def refresh():
    tweetsbox.delete(0, END)
    items = getTweets()
    tweetsbox.insert(END, *items)
    root.after(10000, refresh)


urlLoc = "https://ipapi.co/json"
while True:
    responseLoc = requests.get(urlLoc)
    data = responseLoc.json()
    if "city" in data:
        city = responseLoc.json()["city"]
        break

urlWeather = f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={weatherKey}"
responseWeather = requests.get(urlWeather)
currentTemp = round(responseWeather.json()["main"]["temp"] - 273.15)
currentFeelsLike = round(responseWeather.json()["main"]["feels_like"] - 273.15)
weatherLike = responseWeather.json()["weather"][0]["description"]

messages = getTweets()

root = Tk()
root.title("water mark")
root.geometry("900x480")
root.config(bg="#FFAC00")

mainLabel = Label(master=root, bg="#FFAC00", fg="Black", text="NS Twitter feed", font=("Sans", 30),
                  height=1, width=100)
mainLabel.pack()

subLabel = Label(master=root, bg="#FFAC00", fg="Black", text="Recently submitted messages:",
                 font=("Sans", 15), height=2, width=100)
subLabel.pack()

tweetsbox = Listbox(master=root, bg="#009CDE", fg="White",
                    font=("Sans", 10), height=14, width=140)
tweetsbox.insert(END, *messages)
tweetsbox.pack()

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
