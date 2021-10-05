
# def to create a price based on the inputted trip distance (distanceKM)
def standardPrice(distanceKM):
    if distanceKM <= 0: # If a negative number, or 0, is inputted, the price will be 0
        startprice = 0
    elif distanceKM <= 50: # For trips above 50KM, the cost will be 15 EUR and 60 ct per KM
        startprice = distanceKM * 0.80
    else: # These are trips from 1 to 50 KM, standard price calculation
        startprice = 15 + (distanceKM * 0.60)

    return startprice


# def to use standardPrice(distanceKM) in order to create the final price based on inputs
def travelPrice(age, weekendTrip, distanceKM):
    price = standardPrice(distanceKM)
    if weekendTrip == True: # The following calculations will only happen is it's weekend
        if age >= 65 or age < 12: # For people 65+ and from 0-12 years old, there is a 35% discount in weekends
            finalPrice = price / 100 * 65
            return finalPrice
        else: # For those outside these age groups, the price in weekends has a 40% discount
            finalPrice = price / 100 * 60
            return finalPrice

    if weekendTrip == False: # The following calculations will only happen when it's NOT weekend
        if age >= 65 or age < 12: # Same as above calculation, people in this group receive a 30% discount
            finalPrice = price / 100 * 70
            return finalPrice
        else: # For those outside these age groups, there is no discount outside the weekend
            finalPrice = price
            return finalPrice


# Data inputs below here
distanceKM = int(input("Please fill in your trip's distance: "))
age = int(input("Please fill in your age: "))
weekendTripInput = input("Are you travelling in the weekend? (Y/N) ")
# This checks whether or not it's weekend.
# The user will have to respond with "Y" or "y" in order for weekendTrip to become true
if weekendTripInput == "y" or weekendTripInput == "Y":
    weekendTrip = True
else:
    weekendTrip = False
tripCost = travelPrice(age, weekendTrip, distanceKM)
print("The total cost of your trip will be", round(tripCost, 2), "EUR")
