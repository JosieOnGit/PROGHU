
def inputNumber(optionInput):
    if optionInput == "1":
        print(f"There are {freeLockersCount()} lockers still available.")
    elif optionInput == "2":
        print(newLocker())
    elif optionInput == "3":
        print(openLocker())
    elif optionInput == "4":
        print(returnLocker())
    else:
        print("Please only enter a number between 1-4.")


# With every line being "x;n\", this checks for lines in the text file that has more lines than that.
# Each locker will have a password added next to it if claimed;
# This will increase the line length, thus making it occupied.
def freeLockersCount():
    lockerFile = open("lockers.txt")
    lockers = lockerFile.readlines()
    lockerCount = 0
    for line in lockers:
        if len(line) <= 4:
            lockerCount += 1
        else:
            lockerCount += 0

    return lockerCount


# Opening request
print("1: I want to see the mount of free lockers. \n"
      "2: I want a new locker. \n"
      "3. I want to get something out of my locker. \n"
      "4. I'm returning my locker. \n")

optionInput = input("Please choose one of the above options: ")
inputNumber(optionInput)
