
import psycopg
import requests
import datetime as dt


def review():
    date = dt.datetime.now().strftime("%Y-%m-%d")
    print("----- Welcome to the NS review box! Here you can submit your thoughts about your experiences with NS. \n"
          "----- Your message will be analysed and once approved, you will be able to see it at this station! \n")
    try:
        print("----- The system will now attempt to automatically find which station you're currently at...")
        url = "https://ipapi.co/json"
        response = requests.get(url)
        station = response.json()["city"]
        print("----- Success! \n")
    except:
        station = input("\n----- That didn't work (HTTP/1.1 429 | Too Many Requests). \n"
                        "----- Please manually fill in the station you are currently at. \n"
                        ">> ")
        print("----- Thank you! \n")

    while True:
        messageQ = input("----- You can now leave a message for us here! \n"
                         "----- Please keep it short, as Twitter only allows up to 140 characters. \n"
                         ">> ")
        if 0 < len(messageQ) < 141:
            message = messageQ
            print("----- Thank you! \n")
            break
        else:
            print("----- That didn't work (HTTP/1.1 | 403 Forbidden). \n"
                  "----- That message is too long, please make it shorter. \n")

    name = input("----- Next, please enter your name. \n"
                 "----- You can leave it empty if you wish to stay anonymous. \n"
                 ">> ")
    if name == "":
        name = "Anonymous"

    cur = con.cursor()
    cur.execute("SELECT * FROM twitterdb")
    rows = cur.fetchall()
    messageID = 1
    for item in rows:
        messageID += 1

    pushValues = (messageID, station, name, message, date, 'Pending')
    insert = "INSERT INTO twitterdb (messagenum, station, username, usermessage, submissiondate, modname, status)" \
             "VALUES (%s, %s, %s, %s, %s, NULL, %s)"

    cur.execute(insert, pushValues)
    con.commit()
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
if output is True:
    print("----- Thank you for taking your time to leave a review! \n"
          "----- Your message will be reviewed and appear soon at your current train station.")
else:
    print("Something went wrong, are you sure you did everything right?")
