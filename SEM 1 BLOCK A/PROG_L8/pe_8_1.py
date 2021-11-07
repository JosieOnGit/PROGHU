
numCount = 0
inputSum = 0
while True:
    inputNum = int(input("Please insert a number: "))
    numCount += 1
    inputSum += inputNum
    if inputNum == 0:
        numCount -= 1
        break

print(f"You've inputted {numCount} numbers, the total sum is {inputSum}")
