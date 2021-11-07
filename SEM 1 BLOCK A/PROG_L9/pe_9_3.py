
def code(calculatedValue):
    returnValue = ""
    for letter in calculatedValue:
        returnValue += chr(ord(letter) + 3)
    return returnValue


name = input("Please insert your name: ")
startStation = input("Please insert your departure station: ")
endStation = input("Please insert your arrival station: ")
calculatedValue = name + startStation + endStation
print(code(calculatedValue))
