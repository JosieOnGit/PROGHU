
import datetime as dt
import psycopg
from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)


def review():
    messageDB = open("tweet_list.txt", "r+")
    readMessage = messageDB.readlines()

    date = dt.datetime.now().date()
    time = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    superuser = input("Please enter your last name: ")

    for line in readMessage:
        message = eval(line)["message"]
        station = eval(line)["stationName"]
        name = eval(line)["name"]
        print(f"\"{message}\"")
        print("Please check the above message for any profanity, reliability, etc.")
        approvalQ = input("Do you approve this message? (Y/N): ")
        if approvalQ.lower() == "y":
            print(f"You've approved this message: \"{message}\"\n")

            cur = con.cursor()
            cur.execute("SELECT * FROM twitterdb")
            rows = cur.fetchall()
            messageID = 1
            for item in rows:
                messageID += 1

            pushValues = (messageID, station, name, message, date, superuser, time, 'Approved', '')
            insert = "INSERT INTO twitterdb (messagenum, station, username, usermessage, submissiondate, modname, " \
                     "reviewdate, status, modmessage) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

            cur.execute(insert, pushValues)
            con.commit()
            twitter.update_status(status=message)
            print(f"The following message:\n"
                  f"\"{message}\"\n"
                  f"Has been successfully submitted to Twitter!")

        else:
            removalReason = input("You are rejecting the above message. Please give a reason as to why: ")
            print(f"You've rejected this message: \"{message}\"\n")

            cur = con.cursor()
            cur.execute("SELECT * FROM twitterdb")
            rows = cur.fetchall()
            messageID = 1
            for item in rows:
                messageID += 1

            pushValues = (messageID, station, name, message, date, superuser, time, 'Rejected', removalReason)
            insert = "INSERT INTO twitterdb(messagenum, station, username, usermessage, submissiondate, modname, " \
                     "reviewdate, status, modmessage) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

            cur.execute(insert, pushValues)
            con.commit()

    print("Thank you! This was all for now, please check back soon for new messages!")
    messageDB.close()


# This function cleans the file tweet_list.txt in order to create room for the next messages
def cleanup():
    messageDB = open("tweet_list.txt", "w")
    messageDB.write("")
    messageDB.close()


# This here connects the program to the database
con = psycopg.connect(
    host='localhost',
    dbname='Twitter',
    user='postgres',
    password='admin',
    port=4444
)

# This here connects the program to the Twitter account where the Tweets will be submitted to and shown from
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

review()
cleanup()
