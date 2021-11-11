
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

# Connecting the program to the Twitter handle in order to pull submitted Tweets
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def getTweets():  # Use Twitter API to collect recent tweets
    tweets = api.user_timeline(screen_name="TowaVEVO",
                               count=200,
                               since_id="1457669635093024772",  # Tweets before this ID are gibberish and won't be read
                               include_rts=False,
                               exclude_replies=True,
                               tweet_mode="extended",
                               )
    tweetsLst = []  # The content (full_text) of the Tweets are added to a list
    for info in tweets:
        tweetsLst.append(f"- {info.full_text}")
    return tweetsLst


def refresh():  # Updates the listbox with new Tweets
    tweetsbox.delete(0, END)  # Clears existing list of Tweets
    items = getTweets()  # Executes getTweets to collect new Tweets (if there are any)
    tweetsbox.insert(END, *items)  # All Tweets, including new ones, are added back to the listbox
    root.after(10000, refresh)  # Loops function each 10 seconds


urlLoc = "https://ipapi.co/json"  # Locates city based on IP address location
while True:  # The API might give an error, this loops the request until the correct response is given
    responseLoc = requests.get(urlLoc)
    data = responseLoc.json()
    print("----- Attempting to locate you...")
    if "city" in data:
        city = responseLoc.json()["city"]
        print("----- Success!")
        break

# Using the above location data, we use the weather API to find weather information about said location
urlWeather = f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={weatherKey}"
responseWeather = requests.get(urlWeather)
currentTemp = round(responseWeather.json()["main"]["temp"] - 273.15)
currentFeelsLike = round(responseWeather.json()["main"]["feels_like"] - 273.15)
weatherLike = responseWeather.json()["weather"][0]["description"]

messages = getTweets()  # Yield existing Tweets before looping getTweets()

# GUI built using Tkinter
root = Tk()
root.title("Nederlandse Spoorwegen Twitterzuil")
root.geometry("900x480")
root.iconbitmap("NS_logo.ico")
root.config(bg="#FFAC00")

mainLabel = Label(master=root, bg="#FFAC00", fg="Black", text="NS Twitter feed", font=("Sans", 30),
                  height=1, width=100)
mainLabel.pack()

subLabel = Label(master=root, bg="#FFAC00", fg="Black", text="Recently submitted messages:",
                 font=("Sans", 15), height=2, width=100)
subLabel.pack()

tweetsbox = Listbox(master=root, bg="#003082", fg="White",
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

refresh()  # After packing and creating the GUI, refresh() executes and loops every 10 seconds, infinitely
root.mainloop()
