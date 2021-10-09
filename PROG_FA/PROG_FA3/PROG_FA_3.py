
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
    for locker in content:


    lockerAmount = freeLockersCount()
    if lockerAmount >= 1:
        userCode = input("A free locker is available!\n"
                         "Please input a password for your locker (>4 characters): ")
        if len(userCode) >= 4:
            lockerFile.write(f"{str(lockerAmount)} ; {userCode}\n")
            print(f"Success! You can now open locker {lockerAmount} with your code!")
        else:
            print("Your password isn't long enough, please try again.")


# Opening request
print("1: I want to see the mount of free lockers. \n"
      "2: I want a new locker. \n"
      "3. I want to get something out of my locker. \n"
      "4. I'm returning my locker. \n")

optionInput = input("Please choose one of the above options: ")
inputNumber(optionInput)
