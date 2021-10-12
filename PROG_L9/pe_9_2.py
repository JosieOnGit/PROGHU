
import random


def monopolyThrow():
    throws = 0
    throwsLst = []
    number1 = random.randrange(1, 7)
    number2 = random.randrange(1, 7)
    res = number1 + number2
    while throws != 3:
        if number1 == number2:
            throws += 1
            print(f"{number1} + {number2} = {res}")
            throwsLst.append(f"({number1}, {number2})")
            print(throwsLst)
        elif number1 == number2 and throws == 3:
            print(f"{number1} + {number2} = Go straight to jail.")
            print(throwsLst)
        elif number1 != number2:
            print(f"{number1} + {number2} = {res}")
            throwsLst.append(f"({number1}, {number2})")
            print(throwsLst)
            break


monopolyThrow()
