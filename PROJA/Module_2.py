
import datetime as dt


def review():
    messageDB = open("tweet_list.txt", "r+")
    approvedTweets = open("approved_tweets.txt", "a")
    rejectedTweets = open("rejected_tweets.txt", "a")
    readMessage = messageDB.readlines()

    date = dt.datetime.now().date()
    time = dt.datetime.now().time()

    superuser = input("Please enter your last name: ")
    reviewLine = f"The following messages have been reviewed by {superuser} on {date} at {time}:\n"

    for line in readMessage:
        message = eval(line)["message"]
        print(f"\"{message}\"")
        print("Please check the above message for any profanity, reliability, etc.")
        approvalQ = input("Do you approve this message? (Y/N): ")
        if approvalQ.lower() == "y":
            print(f"You've approved this message: \"{message}\"\n")
            approvedTweets.write(line)
        else:
            print(f"You've rejected this message: \"{message}\"\n")
            rejectedTweets.write(line)

    messageDB.close()
    approvedTweets.close()
    rejectedTweets.close()


def cleanup():
    messageDB = open("tweet_list.txt", "w")
    messageDB.write("")
    messageDB.close()


review()
cleanup()
