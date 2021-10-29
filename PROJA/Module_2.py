import datetime as dt
import psycopg


def review():
    messageDB = open("tweet_list.txt", "r+")
    approvedTweets = open("approved_tweets.txt", "a")
    rejectedTweets = open("rejected_tweets.txt", "a")
    readMessage = messageDB.readlines()

    date = dt.datetime.now().date()
    time = dt.datetime.now().time()

    superuser = input("Please enter your last name: ")
    reviewLine = f"\n---The following messages have been reviewed by {superuser} on {date} at {time}:\n"
    approvedTweets.write(reviewLine)
    rejectedTweets.write(reviewLine)

    for line in readMessage:
        message = eval(line)["message"]
        station = eval(line)["stationName"]
        name = eval(line)["name"]
        print(f"\"{message}\"")
        print("Please check the above message for any profanity, reliability, etc.")
        approvalQ = input("Do you approve this message? (Y/N): ")
        if approvalQ.lower() == "y":
            print(f"You've approved this message: \"{message}\"")
            approvedTweets.write(f"{line}")
            cur = con.cursor()
            cur.execute("SELECT * FROM twitterdb")
            rows = cur.fetchall()
            messageID = 1
            for item in rows:
                messageID += 1
            cur.execute("INSERT INTO twitterdb(messagenum, station, username, usermessage, submissiondate, modname, "
                        "reviewdate, status, modmessage) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (messageID, station, name, message, date, superuser, time, 'Approved', ''))
        else:
            removalReason = input("You are rejecting the above message. Please give a reason as to why: ")
            print(f"You've rejected this message: \"{message}\"\n")
            rejectedTweets.write(f"Rejected for: \"{removalReason}\", {line}")
            cur = con.cursor()
            cur.execute("SELECT * FROM twitterdb")
            rows = cur.fetchall()
            messageID = 1
            for item in rows:
                messageID += 1
            cur.execute("INSERT INTO twitterdb(messagenum, station, username, usermessage, submissiondate, modname, "
                        "reviewdate, status, modmessage) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (messageID, station, name, message, date, superuser, time, 'Rejected', removalReason))

    print("Thank you! This was all for now, please check back soon for new messages!")
    messageDB.close()
    approvedTweets.close()
    rejectedTweets.close()


def cleanup():
    messageDB = open("tweet_list.txt", "w")
    messageDB.write("")
    messageDB.close()


def writeReject():
    print("placeholder")


con = psycopg.connect(
    host='localhost',
    dbname='Twitter',
    user='postgres',
    password='admin',
    port=4444
)

review()
cleanup()
