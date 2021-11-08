
import psycopg
import tweepy
from datetime import datetime
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# Connecting the program to the Twitter handle in order to submit approved messages
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def review():
    # This fetches all messages that have yet to be reviewed, filtering with the status "Pending"
    cur = con.cursor()
    cur.execute("SELECT * FROM twitterdb WHERE status = 'Pending'")
    rows = cur.fetchall()

    superuser = input("----- Please enter your last name. \n"  # Moderator adds their name here for logging changes
                      ">> ")

    for line in rows:  # Each line with "Pending" will be individually checked, loops ends when there are none left
        print(f"----- \"{line[3]}\" \n"
              f"      Please check the above message for any profanity, reliability, etc.")
        approvalQ = input("      Do you approve this message? (Y/N) \n"
                          ">> ")
        if approvalQ.lower() == "y":  # The following will happen if the message is approved:
            # Takes the date AND time of review for the message currently being reviewed
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            print(f"----- You've successfully approved this message: \"{line[3]}\" \n")

            cur = con.cursor()  # Selects the exact message that is being reviewed
            cur.execute("SELECT * FROM twitterdb WHERE status = 'Pending'")
            messageID = line[0]

            pushValues = (superuser, 'Approved', '', timestamp, messageID)
            update = "UPDATE twitterdb " \
                     "SET (modname, status, modmessage, reviewdatetime) = (%s, %s, %s, %s)" \
                     "WHERE messagenum = %s"

            cur.execute(update, pushValues)  # Updates the message being reviewed with the new values
            con.commit()  # Commits the above changes
            try:  # Attempts to push the approved message to the Twitter handle
                print("----- Attempting to push message to Twitter... ")
                api.update_status(line[3])
                print(f"      Message \"{line[3]}\" is published to Twitter! \n")
            except:  # Prints an error if something goes wrong. This might happen if Twitter is down
                print("----- Unknown error \n"
                      "      Something went wrong, we're looking into the issue. \n"
                      "      You might need to manually add the message to Twitter.")

        else:  # The following will happen if the message is rejected:
            # Takes the date AND time of review for the message currently being reviewed
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # The moderator adds a reason why the message in question is being rejected
            removalReason = input("----- You are rejecting the above message. Please give a reason as to why. \n"
                                  ">> ")
            print(f"----- You've successfully rejected this message: \"{line[3]}\" \n")

            cur = con.cursor()  # Selects the exact message that is being reviewed
            cur.execute("SELECT * FROM twitterdb WHERE status = 'Pending'")
            messageID = line[0]

            pushValues = (superuser, 'Rejected', removalReason, timestamp, messageID)
            update = "UPDATE twitterdb " \
                     "SET (modname, status, modmessage, reviewdatetime) = (%s, %s, %s, %s)" \
                     "WHERE messagenum = %s"

            cur.execute(update, pushValues)  # Updates the message being reviewed with the new values
            con.commit()  # Commits the above changes

    # If there are no messages left, the following print will be displayed, and the program will close:
    print("----- There currently are no messages to be reviewed, please check back again soon!")


def yieldApprovals():
    cur = con.cursor()
    cur.execute("SELECT * FROM twitterdb WHERE status = 'Approved'")
    rows = cur.fetchall()
    for line in rows:
        print(f"\"{line[3]}\"")


def yieldRejections():
    cur = con.cursor()
    cur.execute("SELECT * FROM twitterdb WHERE status = 'Rejected'")
    rows = cur.fetchall()
    for line in rows:
        print(f"\"{line[3]}\"")


# This here connects the program to the database
con = psycopg.connect(
    host='localhost',
    dbname='Twitter',
    user='postgres',
    password='admin',
    port=4444
)

while True:
    selection = input("\n----- Welcome, moderator. \n"
                      "      Please select one of the below options: \n"
                      "      1. Review new messages \n"
                      "      2. View approved messages \n"
                      "      3. View rejected messages \n"
                      "      4. Exit \n"
                      ">> ")
    if selection == "1":
        review()
    elif selection == "2":
        yieldApprovals()
    elif selection == "3":
        yieldRejections()
    elif selection == "4":
        print("----- Closing the program...")
        quit()
    else:
        print("----- Please only insert a number ranging from 1-4.")

