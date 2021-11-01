
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
photo = open("C:\\Users\\TheBl\\Downloads\\q6edqb41wts71.png", "rb")
response = twitter.upload_media(media=photo)
twitter.update_status(media_ids=[response['media_id']])
