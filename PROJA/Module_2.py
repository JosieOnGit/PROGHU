
def review():
    messageDB = open("tweet_list.txt", "r+")
    approvedTweets = open("approved_tweets.txt", "a")
    rejectedTweets = open("rejected_tweets.txt", "a")
    readMessage = messageDB.readlines()
    for line in readMessage:
        message = line.strip().split(sep=", ")
        print("\"" + message[-1] + "\"")
        print("Please check the above message for any profanity, reliability, and others.")
        approvalQ = input("Do you approve this message? (Y/N) ")
        if approvalQ.lower() == "y":
            print("You've approved this message: " + message[-1] + "\n")
            approvedTweets.write("Approved, " + line)
        else:
            print("You've rejected this message: " + message[-1] + "\n")
            rejectedTweets.write("Rejected, " + line)

    print("That was all, thank you for reviewing the new messages!")
    messageDB.close()
    approvedTweets.close()


def cleanup():
    messageDB = open("tweet_list.txt", "w")
    messageDB.write("")
    messageDB.close()


review()
cleanup()
