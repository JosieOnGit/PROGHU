
def inputDeparture(stations):
    stationsLst = stations
    while True:
        departureStation = input("What station will you depart from?\n"
                                 ">> ")
        if departureStation.capitalize() in stationsLst:
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
        if arrivalIndex < departureIndex:
            print(f"{arrivalStation.capitalize()} is located before {departure}.\n"
                  f"Please choose a train station that comes after {departure}, not before.\n"
                  f"Alternatively, please try again with the opposite traject (Maastricht >> Schagen).")
        elif arrivalIndex == departureIndex:
            print(f"You are already at {departure}.")
        elif arrivalStation.capitalize() in stationsLst and arrivalIndex > departureIndex:
            return arrivalStation.capitalize()
        else:
            print(f"{arrivalStation.capitalize()} isn't on this traject, please try again.")


def outputTrip(stations, departure, arrival):
    stationsLst = stations
    departureIndex = stations.index(departure)
    departureStation = stations.index(departure) + 1
    arrivalIndex = stations.index(arrival)
    arrivalStation = stations.index(arrival) + 1
    distance = arrivalIndex - departureIndex
    price = distance * 5

    stops = ""
    for station in range(departureIndex + 1, arrivalIndex):
        stops += f"  - {stationsLst[station]}\n"

    result = f"Departure station {stationsLst[departureIndex]} is station {departureStation} on this traject.\n" \
             f"Arrival station {stationsLst[arrivalIndex]} is station {arrivalStation} on this traject.\n" \
             f"Your trip crosses {distance} stations.\n" \
             f"The cost of this trip will be €{price}\n" \
             f"You will board the train in: {stationsLst[departureIndex]}\n" \
             f"Passing the following stations:\n" \
             f"{stops}" \
             f"Until you'll exit the train again in: {stationsLst[arrivalIndex]}"

    return result


stations = ["Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk", "Amsterdam Centraal",
            "Amsterdam Amstel", "Utrecht Centraal", "'s-Hertogenbosch", "Eindhoven", "Weert", "Roermond", "Sittard",
            "Maastricht"]
departure = inputDeparture(stations)
arrival = inputArrival(stations, departure)
output = outputTrip(stations, departure, arrival)
print(output)
