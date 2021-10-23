
def inputDeparture(stations):
    stationsLst = stations
    stationInLst = False
    while stationInLst is False:
        departureStation = input("What station will you depart from?\n"
                                 ">> ")
        departureIndex = 1
        for station in stationsLst:
            if departureStation.capitalize() != station:
                departureIndex += 1
        if departureStation.capitalize() in stationsLst:
            stationInLst = True
            return departureStation.capitalize()
        else:
            print(f"\"{departureStation.capitalize()}\" isn't on this traject, please try again.")


def inputArrival(stations, departure):
    departureIndex = stations.index(departure)
    stationsLst = stations
    stationInLst = False
    while stationInLst is False:
        arrivalStation = input("What station will you be arriving at?\n"
                               ">> ")
        arrivalIndex = 0
        for station in stationsLst:
            if arrivalStation.capitalize() != station:
                arrivalIndex += 1
            else:
                break
        if arrivalStation.capitalize() in stationsLst and arrivalIndex > departureIndex:
            return arrivalStation.capitalize()
        else:
            print("That didn't work, please try again.")


def outputTrip(stations, departure, arrival):
    stationsLst = stations
    departureIndex = stations.index(departure)
    departureStation = stations.index(departure) + 1
    arrivalIndex = stations.index(arrival)
    arrivalStation = stations.index(arrival) + 1
    distance = arrivalIndex - departureIndex
    price = distance * 5
    print(f"Departure station {stationsLst[departureIndex]} is station {departureStation} on this traject.\n"
          f"Arrival station {stationsLst[arrivalIndex]} is station {arrivalStation} on this traject.\n"
          f"Your trip crosses {distance} stations.\n"
          f"The cost of this trip will be €{price}\n"
          "\n"
          f"You will board the train in {stationsLst[departureIndex]}\n"
          f"Passing the following stations:")
    currentStation = departureIndex
    for station in range(departureIndex, arrivalIndex):
        if currentStation + 1 == arrivalIndex:
            continue
        else:
            currentStation += 1
            print(f"  - {stationsLst[currentStation]}")
    print(f"Until you'll exit the train again in {stationsLst[arrivalIndex]}")
    return departureStation, arrivalStation, distance, price


stations = ["Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk", "Amsterdam Centraal",
            "Amsterdam Amstel", "Utrecht Centraal", "'s-Hertogenbosch", "Eindhoven", "Weert", "Roermond", "Sittard",
            "Maastricht"]
departure = inputDeparture(stations)
arrival = inputArrival(stations, departure)
output = outputTrip(stations, departure, arrival)
print(output)
