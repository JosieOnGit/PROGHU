
def inputNumber(optionInput):
    if optionInput == "1":
        print(f"There are {freeLockersCount()} lockers still available.")
    elif optionInput == "2":
        newLocker()
    elif optionInput == "3":
        openLocker()
    elif optionInput == "4":
        returnLocker()
    else:
        print("Please only enter a number between 1-4.")


# With every line being "x;n\", this checks for lines in the text file that has more lines than that.
# Each locker will have a password added next to it if claimed;
# This will increase the line length, thus making it occupied.
def freeLockersCount():
    lockerFile = open("lockers.txt")
    occupiedLockers = len(lockerFile.readlines())
    lockerAmount = 12 - occupiedLockers
    lockerFile.close()
    return int(lockerAmount)


def newLocker():
    lockerFile = open("lockers.txt", "r+")
    content = lockerFile.readlines()
    lockerFile.close()
    for locker in range(1, 13):
        lockerClaimed = False
        for var in content:
            if str(locker) in var:
                lockerClaimed = True
        if lockerClaimed == False:
            while True:
                lockerFile = open("lockers.txt", "a")
                password = input("Please insert a password for your locker (4 or more characters): ")
                if len(password) >= 4:
                    lockerFile.write(f"{locker};{password}\n")
                    print("Success! Check the file to see your new locker added.")
                    break
                else:
                    print("That didn't work. Please insert a password of 4 characters or longer.")


def openLocker():
    print("placeholder")


def returnLocker():
    print("placeholder")


# Opening request
print("1: I want to see the amount of free lockers. \n"
      "2: I want a new locker. \n"
      "3. I want to get something out of my locker. \n"
      "4. I'm returning my locker. \n")

optionInput = input("Please choose one of the above options: ")
inputNumber(optionInput)
