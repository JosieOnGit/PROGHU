
def review(message, station, name):
    messagesDB = open("tweet_list.txt", "a")

    form = {
        "stationName": station,
        "name": name,
        "message": message
    }
    if len(message) <= 140:
        messagesDB.write(f"{form}\n")
        return 1

    else:
        return 0


message = input("Please leave a message for us! ")
station = input("At which station were you writing this message? ")
nameQ = input("Would you like to include your name? (You will remain anonymous if you choose not to) (Y/N): ")
if nameQ.lower() == "y":
    name = input("Please fill in your name here: ")
elif nameQ.lower() == "n":
    name = "Anonymous"
else:
    print("That didn't work. \n"
          "Please restart and answer either Y (Yes) or N (No) \n")
    # Ends the program early to avoid getting errors when trying to execute review(message, station, name)
    quit()
output = review(message, station, name)

if output == 1:
    print("Thank you for leaving your message! \n"
          "Your message will now be reviewed and appear soon at your train station.")
elif output == 0:
    print("This message is too long (max. 140 characters) \n"
          "We only support messages up to 140 characters. Please restart and try again.")
else:
    print("Something went wrong, are you sure you did everything right?")
