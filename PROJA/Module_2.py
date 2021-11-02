
import datetime as dt
import psycopg
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


def review():
    cur = con.cursor()
    cur.execute("SELECT * FROM twitterdb WHERE status = 'Pending'")
    rows = cur.fetchall()

    superuser = input("----- Please enter your last name. \n"
                      ">> ")

    for line in rows:
        print(f"----- \"{line[3]}\" \n"
              f"----- Please check the above message for any profanity, reliability, etc.")
        approvalQ = input("----- Do you approve this message? (Y/N) \n"
                          ">> ")
        if approvalQ.lower() == "y":
            timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            print(f"----- You've successfully approved this message: \"{line[3]}\" \n")

            cur = con.cursor()
            cur.execute("SELECT * FROM twitterdb WHERE status = 'Pending'")
            messageID = line[0]

            pushValues = (superuser, 'Approved', '', timestamp, messageID)
            update = "UPDATE twitterdb " \
                     "SET (modname, status, modmessage, reviewdatetime) = (%s, %s, %s, %s)" \
                     "WHERE messagenum = %s"

            cur.execute(update, pushValues)
            con.commit()
            try:
                print("----- Attempting to push message to Twitter... ")
                api.update_status(line[3])
                print(f"----- Message \"{line[3]}\" is published to Twitter! \n")
            except:
                print("----- Unknown error \n"
                      "Something went wrong, we're looking into the issue. \n"
                      "You might need to manually add the message to Twitter.")

        else:
            timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            removalReason = input("----- You are rejecting the above message. Please give a reason as to why. \n"
                                  ">> ")
            print(f"----- You've successfully rejected this message: \"{line[3]}\" \n")

            cur = con.cursor()
            cur.execute("SELECT * FROM twitterdb WHERE status = 'Pending'")
            messageID = line[0]

            pushValues = (superuser, 'Rejected', removalReason, timestamp, messageID)
            update = "UPDATE twitterdb " \
                     "SET (modname, status, modmessage, reviewdatetime) = (%s, %s, %s, %s)" \
                     "WHERE messagenum = %s"

            cur.execute(update, pushValues)
            con.commit()

    print("----- Thank you! This was all for now, please check back soon for new messages!")


# This here connects the program to the database
con = psycopg.connect(
    host='localhost',
    dbname='Twitter',
    user='postgres',
    password='admin',
    port=4444
)

review()
