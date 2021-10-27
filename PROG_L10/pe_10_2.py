
# Dit programma gaat er van uit dat pe_10_2_users.json al bestaat
import json


def addForm():
    with open(file, "r") as loadFile:
        lst = json.load(loadFile)
        lst.append(form)

    with open(file, "w") as writeFile:
        json.dump(lst, writeFile, indent=4)


file = "pe_10_2_users.json"

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
        addForm()

    except json.decoder.JSONDecodeError:
        emptyLst = []
        with open(file, "w") as writeFile:
            json.dump(emptyLst, writeFile)

        addForm()
        continue
