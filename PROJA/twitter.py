
from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

message = "no more data i deleted it all"
twitter.update_status(status=message)
print("Tweeted: %s" % message)
