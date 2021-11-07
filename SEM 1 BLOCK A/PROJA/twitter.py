
import tweepy
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.get_user(screen_name="NeneVEVO")
tweets = api.user_timeline(screen_name="TowaVEVO",
                           count=200,
                           include_rts=False,
                           tweet_mode="extended"
                           )

for info in tweets:
    print(f"ID : {info.id}")
    print(info.created_at)
    print(f"{info.full_text}\n")

message = input(">> ")
# api.update_status(message)
print(f"\"{message}\" was successfully submitted to Twitter!")
