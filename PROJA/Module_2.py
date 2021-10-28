
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
        print(f"\"{message}\"")
        print("Please check the above message for any profanity, reliability, etc.")
        approvalQ = input("Do you approve this message? (Y/N): ")
        if approvalQ.lower() == "y":
            print(f"You've approved this message: \"{message}\"")
            approvedTweets.write(f"{line}")
        else:
            removalReason = input("You are rejecting the above message. Please give a reason as to why: ")
            print(f"You've rejected this message: \"{message}\"\n")
            rejectedTweets.write(f"Rejected for: \"{removalReason}\", {line}")

    print("Thank you! This was all for now, please check back soon for new messages!")
    messageDB.close()
    approvedTweets.close()
    rejectedTweets.close()


def cleanup():
    messageDB = open("tweet_list.txt", "w")
    messageDB.write("")
    messageDB.close()


def connectDB():
    con = psycopg.connect(
        host='localhost',
        dbname='postgres',
        user='postgres',
        password='admin',
        port=4444
    )


def writeApprove():
    print("placeholder")


def writeReject():
    print("placeholder")


review()
cleanup()
