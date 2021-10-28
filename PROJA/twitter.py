
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

message = "Tokoyami Towa (常闇トワ) is a female Japanese Virtual YouTuber associated with hololive, debuting as part of its fourth generation of VTubers al"
twitter.update_status(status=message)
print("Tweeted: %s" % message)
