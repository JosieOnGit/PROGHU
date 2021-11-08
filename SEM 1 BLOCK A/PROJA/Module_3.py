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


def refresh():
    counter = 1
    print(f"Picked some random Tweets!")
    text1Label["text"] = random.choice(tweetsLst)
    text2Label["text"] = random.choice(tweetsLst)
    if text1Label["text"] == text2Label["text"]:
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

root = Tk()
root.title("My kids are in the basement please give them water pelase please please i beg you")
root.geometry("900x480")
root.config(bg="#FFAC00")
root.iconbitmap("C:\\Users\\Josie\\Downloads\\linus.ico")

mainLabel = Label(master=root, bg="#FFAC00", fg="Black", text="NS Twitter feed", font=("Sans", 30),
                  height=1, width=100)
mainLabel.pack()

subLabel = Label(master=root, bg="#FFAC00", fg="Black", text="Some submitted messages:", font=("Sans", 15),
                 height=2, width=100)
subLabel.pack()

text1Label = Label(master=root, bg="#009CDE", text=random.choice(tweetsLst), font=("Sans", 15),
                   height=2, width=100, wraplength=800)
text1Label.pack()

text2Label = Label(master=root, bg="#009CDE", text=random.choice(tweetsLst), font=("Sans", 15),
                   height=2, width=100, wraplength=800)
text2Label.pack()

# listbox = Listbox(master=root, bg="White", height=20)
# listbox.pack(fill=X, expand=YES)

refresh()
root.mainloop()
