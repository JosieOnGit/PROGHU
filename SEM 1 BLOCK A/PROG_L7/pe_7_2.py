
def analyzer(numbers):
    # Temp list for converting string input to int
    hold = numbers.split(sep="-")
    numList = []
    for i in hold:
        numList.append(int(i))
    # Prints out numList
    print(f"Sorted list of inputted ints: {numList}")
    # Calculates and prints min/max
    maxValue = max(numList)
    minValue = min(numList)
    print(f"Greatest number: {maxValue} and smallest number: {minValue}")
    # Calculates and prints len/sum
    lenList = int(len(numList))
    sumList = sum(numList)
    print(f"Amount of numbers: {lenList} and sum of all numbers: {sumList}")
    # Calculates and prints average
    avgList = sumList / lenList
    print(f"Average: {avgList}")

    return numList, maxValue, minValue, lenList, sumList, avgList


numbers = input("Please input a series of numbers. (e.g. 5-7-8-9): ")
analyzer(numbers)

