
import tweepy
import random
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


def refreshItem():
    labelText["text"] = random.choice(tweetsLst)


tweets = api.user_timeline(screen_name="TowaVEVO",
                           count=200,
                           include_rts=False,
                           exclude_replies=True,
                           tweet_mode="extended",
                           )
tweetsLst = []
for info in tweets:
    tweetsLst.append(info.full_text)

root = Tk()
root.geometry("900x480")

labelText = Label(master=root, text=random.choice(tweetsLst), font=("Helvetica", 25, "bold"))
labelText.pack()

buttonRefresh = Button(master=root, text="Click here to refresh!", command=refreshItem)
buttonRefresh.pack(fill=X)

root.mainloop()
