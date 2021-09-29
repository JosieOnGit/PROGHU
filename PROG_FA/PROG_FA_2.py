
def standardprice(distanceKM):
    price = distanceKM * 0.80
    if distanceKM <= 0:
        startPrice = 0

    elif distanceKM > 50:
        startPrice = 15 + (distanceKM * 0.60)

    else:
        startPrice = distanceKM * 0.80

    return startPrice


def travelPrice(age, weekendTrip, distanceKM):
    if weekendTrip == True:
        if 65 >= age or 12 > age:
            finalPrice = standardprice(distanceKM) * 0.65
            return finalPrice
        if 65 > age or 12 <= age:
            finalPrice = standardprice(distanceKM) / 100 * 60
            return finalPrice

    if weekendTrip == False:
        if 65 >= age or 12 > age:
            finalPrice = standardprice(distanceKM) * 0.7
            return finalPrice
        if 65 > age or 12 < age:
            finalPrice = standardprice(distanceKM)
            return finalPrice


distanceKM = int(input("Please fill in your trip's distance: "))
age = int(input("Please fill in your age: "))
weekendTripInput = input("Are you travelling in the weekend? (Y/N) ")
if weekendTripInput == "y" or weekendTripInput == "Y":
    weekendTrip = True
else:
    weekendTrip = False
tripCost = travelPrice(age, weekendTrip, distanceKM)
print("The total cost of your trip will be", round(tripCost, 2), "EUR")
