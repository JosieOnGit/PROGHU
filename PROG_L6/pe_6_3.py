
def numLines():
    file = open("pe_6_2_cardnumbers.txt")
    lineList = file.readlines()
    file.close()
    print("This file has {} lines".format(len(lineList)))
    return len(lineList)


def maxNumber():
    file = open("pe_6_2_cardnumbers.txt")
    content = file.readlines()
    cardNumber = max(content)
    maxNumber = cardNumber.strip().split(sep=", ")
    for number in maxNumber:
        if number in "0123456789":
            char = number
    lineNum = content.index(cardNumber) + 1
    file.close()
    print("The greatest card number is: {} and is located on line {}".format(maxNumber[0], lineNum))
    return lineNum, maxNumber


numLines()
maxNumber()
