
import psycopg
import requests
from datetime import datetime


def review():
    # Yields the current date the message is being written at
    date = datetime.now().strftime("%Y-%m-%d")
    print("----- Welcome to the NS review box! Here you can submit your thoughts about your experiences with NS. \n"
          "      Your message will be analysed and once approved, you will be able to see it at this station! \n")
    try:  # Attempts to get city data from the pillar's API
        print("----- The system will now attempt to automatically find which station you're currently at...")
        url = "https://ipapi.co/json"
        response = requests.get(url)
        station = response.json()["city"]
        print(f"      Success! You are currently in {station}. \n")
    except:  # If the above fails, the user submits the location they are at themselves
        print("----- That didn't work (Location data error: HTTP/1.1 | 429 Too Many Requests.)")
        station = input("\n----- Something went wrong while trying to locate the station you're at. \n"
                        "      Please manually fill in the station you are currently at. \n"
                        ">> ")
        print("----- Thank you! \n")

    while True:  # Loops request until the correct flow is achieved (Message is under 141 characters)
        messageQ = input("----- You can now leave a message for us here! \n"
                         "      Please keep it short, as Twitter only allows up to 140 characters. \n"
                         ">> ")
        if 0 < len(messageQ) <= 140:
            message = messageQ
            print("----- Thank you! \n")
            break
        else:  # Basic error output with info on the submitted length being larger than 140 chars
            print("----- That didn't work (Submission error: HTTP/1.1 | 403 Forbidden.) \n"
                  f"      That message is too long ({len(messageQ)} > 140), please make it shorter. \n")

    # Basic name input, if left empty, the name will automatically become "Anonymous"
    name = input("----- Next, please enter your name. \n"
                 "      You can leave it empty if you wish to stay anonymous. \n"
                 ">> ")
    if name == "":
        name = "Anonymous"

    # Program connects to the database and selects all rows to create the messageID
    cur = con.cursor()
    cur.execute("SELECT * FROM twitterdb")
    rows = cur.fetchall()
    messageID = 1
    for item in rows:
        messageID += 1

    # Values to be pushed paired with the SQL query
    # "Pending" is added as the value for "status". This will be used to filter unreviewed messages in Module 2
    pushValues = (messageID, station, name, message, date, 'Pending')
    insert = "INSERT INTO twitterdb (messagenum, station, username, usermessage, submissiondate, modname, status)" \
             "VALUES (%s, %s, %s, %s, %s, NULL, %s)"

    cur.execute(insert, pushValues)  # Query execution with all correct values
    con.commit()  # Committing changed to DB
    return True


# This here connects the program to the database
con = psycopg.connect(
    host='localhost',
    dbname='Twitter',
    user='postgres',
    password='admin',
    port=4444
)

output = review()
if output is True:  # Simple program completion output
    print("----- Thank you for taking your time to leave a review! \n"
          "      Your message will be reviewed and appear soon at your current train station.")
else:  # If the program someone returns anything other than "True", this error will be displayed
    print("----- The program ran into an exceptional error, that can't be fixed at this very moment.\n"
          "      Please ask the on-location staff for assistance, thank you for your patience.")
