
import json

file = "pe_10_2_users.json"

while True:
    name = input("What is your name? ")
    letters = input("What are your names' letters? ")
    bday = input("What is your birthdate? ")
    email = input("What is your e-mail address? ")

    form = {
        "name": name,
        "letters": letters,
        "bday": bday,
        "email": email
    }

    with open(file, "a") as file:
        json.dump(form, file, indent=4)
