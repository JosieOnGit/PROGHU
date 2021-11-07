
def length(length=int(input("How tall are you? "))):
    if length >= 120:
        print("You can ride this attraction!")

    else:
        print("Sorry! You're not tall enough to ride this attraction!")
        return length


length(length)
