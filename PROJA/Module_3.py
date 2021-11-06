
import tweepy
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

root = Tk()
tweets = api.user_timeline(screen_name="TowaVEVO",
                           count=200,
                           include_rts=False,
                           tweet_mode="extended"
                           )
for info in tweets:
    print(info.full_text)
