
import json

while True:
    name = input("What is your name? ")
    if name == "quit":
        break
    letters = input("What are your names' letters? ")
    bday = input("What is your birthdate? ")
    email = input("What is your e-mail address? ")

    form = {
        "name": name,
        "letters": letters,
        "bday": bday,
        "email": email
    }
    try:
        with open("pe_10_2_users.json", "r") as loadFile:
            lst = json.load(loadFile)
            lst.append(form)

        with open("pe_10_2_users.json", "w") as writeFile:
            json.dump(lst, writeFile, indent=4)

    except json.decoder.JSONDecodeError:
        emptyLst = []
        with open("pe_10_2_users.json", "w") as writeFile:
            json.dump(emptyLst, writeFile)

        with open("pe_10_2_users.json", "r") as loadFile:
            lst = json.load(loadFile)
            lst.append(form)

        with open("pe_10_2_users.json", "w") as writeFile:
            json.dump(lst, writeFile, indent=4)
        continue
