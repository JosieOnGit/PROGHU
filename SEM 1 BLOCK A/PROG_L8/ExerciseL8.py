
# While loop exercise
def sum():
    total = 0
    while True:
        nextInt = input("Next int: ")
        if nextInt.lower() == "quit":
            break
        total += int(nextInt)
    print(f"The total amount is {total}")


sum()
