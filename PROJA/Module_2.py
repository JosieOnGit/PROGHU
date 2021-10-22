
def review():
    messageDB = open("tweet_list.txt", "r+")
    approvedTweets = open("approved_tweets.txt", "a")
    rejectedTweets = open("rejected_tweets.txt", "a")
    readMessage = messageDB.readlines()
    for line in readMessage:
        message = eval(line)["message"]
        print(f"\"{message}\"")
        print("Please check the above message for any profanity, reliability, etc.")
        approvalQ = input("Do you approve this message? (Y/N) ")
        if approvalQ.lower() == "y":
            print(f"You've approved this message: \"{message}\"\n")
            approvedTweets.write(line)
        else:
            print(f"You've rejected this message: \"{message}\"\n")
            rejectedTweets.write(line)

    print("That was all, thank you for reviewing the new messages!")
    messageDB.close()
    approvedTweets.close()
    rejectedTweets.close()


def cleanup():
    messageDB = open("tweet_list.txt", "w")
    messageDB.write("")
    messageDB.close()


review()
cleanup()
