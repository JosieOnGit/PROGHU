# Analysing and removing vowels from a given text
def noVowels(text):
    newText = ""
    for letter in text:
        if letter not in "aeiou":
            newText += letter
    return newText


text = input("Please put in a quick text! \n"
             ">> ")
print(noVowels(text))


# Analysing and receiving a random amount of numbers, then calculating the average of said numbers
def avg():
    numLst = numInput()
    total = 0
    for num in numLst:
        total += num
    avg = total / len(numLst)
    return avg


def numInput():
    numLst = []
    while True:
        num = int(input("Please input a number! \n"
                        ">> "))
        if num == 0:
            break
        else:
            numLst.append(num)
    return numLst


print(avg())


# Linear searching: Find it the element "target" exists in "lst"
def linearSearch(lst, target):
    for item in lst:
        if target == item:
            return True
    return False


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = int(input("Please insert a number to find in the list \n"
                   ">> "))
print(linearSearch(lst, target))
