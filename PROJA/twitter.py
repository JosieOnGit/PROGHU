
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

user = api.get_user(screen_name="TowaVEVO")
print(user.followers_count)

message = input(">> ")
api.update_status(message)
print(f"\"{message}\" was successfully submitted to Twitter!")
