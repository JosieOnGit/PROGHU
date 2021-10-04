
def review(message, station, name):
    messagesDB = open("tweet_list.txt", "a")

    if len(message) <= 140:
        messagesDB.write(station + ", " + name + ", " + message + "\n")
        print("Thank you for leaving your message! \n"
              "Your message will now be reviewed and appear soon at your train station.")
    else:
        print("This message is too long (max. 140 characters) \n"
              "We only support messages up to 140 characters. Please restart and try again.")


message = input("Please leave a message for us! ")
station = input("At which station were you writing this message? ")
nameQ = input("Would you like to include your name? (You will remain anonymous if you choose not to) (Y/N): ")
if nameQ.lower() == "y":
    name = input("Please fill in your name here: ")
elif nameQ.lower() == "n":
    name = "Anonymous"
else:
    print("That didn't work. \n"
          "Please restart and answer either Y (Yes) or N (No)")
    # Ends the program early to avoid getting errors when trying to execute review(message, station, name)
    quit()
review(message, station, name)
