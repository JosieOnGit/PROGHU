
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

message = "twython.exceptions.TwythonError: Twitter API returned a 403 (Forbidden), Tweet needs to be a bit shorter."
twitter.update_status(status=message)
print("Tweeted: %s" % message)
