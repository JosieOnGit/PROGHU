
def review(message, station, name):
    messagesDB = open("tweet_list.txt", "a")

    form = {
        "stationName": station,
        "name": name,
        "message": message
    }
    while True:
        if len(message) <= 140:
            messagesDB.write(f"{form}\n")
            return True
        else:
            print("This message is too long (max. 140 characters) \n"
                  "We only support messages up to 140 characters. Please shorten your message and try again.")


message = input("Please leave a message for us! ")
station = input("At which station were you writing this message? ")
while True:
    nameQ = input("Would you like to include your name? (You will remain anonymous if you choose not to) (Y/N): ")
    if nameQ.lower() == "y":
        name = input("Please fill in your name here: ")
        break
    elif nameQ.lower() == "n":
        name = "Anonymous"
        break
    else:
        print("That didn't work. \n"
              "Please answer either Y (Yes) or N (No) \n")

output = review(message, station, name)
if output is True:
    print("Thank you for leaving your message! \n"
          "Your message will now be reviewed and appear soon at your train station.")
else:
    print("Something went wrong, are you sure you did everything right?")
