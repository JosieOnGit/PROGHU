
def inputNumber(optionInput):
    if optionInput == "1":
        print(f"There are {freeLockersCount()} lockers still available.")
    elif optionInput == "2":
        output2 = newLocker()
        if output2 == -2:
            print("Sorry! There aren't any free lockers left.")
        elif output2 == -1:
            print("That didn't work. Are you sure you did everything right?")
        elif output2 == 0:
            print("Success! Program closing.")
    elif optionInput == "3":
        openLocker()
    elif optionInput == "4":
        returnLocker()
    elif optionInput == "5":
        print("Closing the program.")
    else:
        print("Please only enter a number between 1-5.")


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
    if freeLockersCount() == 0:
        return -2
    for locker in range(1, 13):
        lockerClaimed = False
        for var in content:
            if str(locker) in var:
                lockerClaimed = True
        if lockerClaimed is False:
            lockerFile = open("lockers.txt", "a")
            password = input("Please insert a password for your locker (4 or more characters): ")
            checkPassword = ""
            if ";" in password or len(password) < 4:
                return -1
            else:
                checkPassword = True

            if checkPassword is True:
                lockerFile.write(f"{locker};{password}\n")
                print(f"Success! You can now open locker {locker}.")
                lockerFile.close()
                return 0
            return -1


def openLocker():
    lockerFile = open("lockers.txt", "r")
    content = lockerFile.readlines()
    lockerFile.close()
    lockerNum = int(input("Please fill in your locker number: "))
    for line in content:
        if str(lockerNum) in line:
            password = str(lockerNum) + ";" + input("Please fill in your password: ") + "\n"
            if password == line:
                print(f"Success! You can now open your locker ({lockerNum})!")
                return True
            else:
                print("That didn't work. Are you sure you have the right locker/password combination?")
                return False


def returnLocker():
    print("placeholder")


# Opening request
print("1: I want to see the amount of free lockers. \n"
      "2: I want a new locker. \n"
      "3. I want to get something out of my locker. \n"
      "4. I'm returning my locker. \n"
      "5. Cancel.\n")

optionInput = input("Please choose one of the above options: ")
inputNumber(optionInput)
