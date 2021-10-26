
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
    with open(file, "r") as file:
        content = json.load(file)

    with open("pe_10_2_users.json", "w") as file:
        json.dump(content, form, indent=4)
