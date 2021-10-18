#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback, collections, builtins

"""
Programming
Final assignment 4: NS-kaartauatomaat
(c) 2021 Hogeschool Utrecht,
Tijmen Muller en 
Bart van Eijkelenburg (bart.vaneijkelenburg@hu.nl)


Opdracht:
Werk onderstaande functies uit.
Voeg commentaar toe om je code toe te lichten.
Lever je werk in op Canvas als alle tests slagen.
"""


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
          f"You will board the train in: {stationsLst[departureIndex]}\n"
          f"Passing the following stations:")
    currentStation = departureIndex
    for station in range(departureIndex, arrivalIndex):
        if currentStation + 1 == arrivalIndex:
            continue
        else:
            currentStation += 1
            print(f"  - {stationsLst[currentStation]}")
    print(f"Until you'll exit the train again in: {stationsLst[arrivalIndex]}")
    return departureStation, arrivalStation, distance, price


def development_code():
    # Gebruik (delen van) deze code om je functies te testen tijdens het programmeren:
    stations = ["Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk",
                "Amsterdam Centraal",
                "Amsterdam Amstel", "Utrecht Centraal", "s-Hertogenbosch", "Eindhoven", "Weert", "Roermond", "Sittard",
                "Maastricht"]
    departure = inputDeparture(stations)
    arrival = inputArrival(stations, departure)
    outputTrip(stations, departure, arrival)


def module_runner():
    # development_code()  # Comment deze regel om je 'development_code' uit te schakelen
    __run_tests()       # Comment deze regel om de HU-tests uit te schakelen


"""
==========================[ HU TESTRAAMWERK ]================================
Hieronder staan de tests voor je code -- daaraan mag je niets wijzigen!
"""


def __my_assert_args(function, args, expected_output, check_type=False):
    """
    Controleer of gegeven functie met gegeven argumenten het verwachte resultaat oplevert.
    Optioneel wordt ook het return-type gecontroleerd.
    """
    argstr = str(args).replace(',)', ')')
    output = function(*args)

    # Controleer eerst het return-type (optioneel)
    if check_type:
        msg = f"Fout: {function.__name__}{argstr} geeft geen {type(expected_output).__name__} terug als return-type"
        assert type(output) is type(expected_output), msg

    # Controleer of de functie-uitvoer overeenkomt met de gewenste uitvoer
    if str(expected_output) == str(output):
        msg = f"Fout: {function.__name__}{argstr} geeft {output} ({type(output).__name__}) " \
              f"in plaats van {expected_output} (type {type(expected_output).__name__})"
    else:
        msg = f"Fout: {function.__name__}{argstr} geeft {output} in plaats van {expected_output}"

    if type(expected_output) is float and isinstance(output, (int, float, complex)):
        # Vergelijk bij float als return-type op 7 decimalen om afrondingsfouten te omzeilen
        assert round(output - expected_output, 7) == 0, msg
    else:
        assert output == expected_output, msg


def __stations():
    return ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk',
            'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "’s-Hertogenbosch", 'Eindhoven', 'Weert',
            'Roermond', 'Sittard', 'Maastricht']


def __out_of_input_error():
    raise AssertionError("Fout: er werd in de functie vaker om input gevraagd dan verwacht.")


def __check_testcase(simulated_input, function, function_args, expected_output):
    original_input = builtins.input
    simulated_input_copy = simulated_input.copy()
    simulated_input.reverse()
    builtins.input = lambda prompt="": simulated_input.pop() if len(simulated_input) > 0 else __out_of_input_error()

    try:
        __my_assert_args(function, function_args, expected_output)
    except AssertionError as ae:
        raise AssertionError(f"{ae.args[0]}\n -> Info: gesimuleerde input voor deze test: {simulated_input_copy}.") from ae
    finally:
        builtins.input = original_input


def test_inlezen_beginstation():
    function = inputDeparture

    case = collections.namedtuple('case', 'simulated_input expected_start')
    testcases = [ case(["asfasf", "Schagen", "Alkmaar"], "Schagen"),
                  case(["Sittard" ], "Sittard"),
                  case(["Alkmr", "Alkmeer", "Alkmaar"], "Alkmaar") ]

    for test in testcases:
        __check_testcase(test.simulated_input, function, (__stations(),), test.expected_start)


def test_inlezen_eindstation():
    function = inputArrival

    case = collections.namedtuple('case', 'simulated_input start expected_stop')
    testcases = [ case(["asfasf", "Schagen", "Maastricht" ], "Schagen", "Maastricht"),
                  case(["asfsdf", "Schagen", "Alkmaar", "asfdfa", "Maastricht" ], "Alkmaar", "Maastricht"),
                  case(["Groningen", "Schagen", "Dedemsvaart", "Zaltbommel", "Eindhoven", "Den Briel" ], "Alkmaar", "Eindhoven")]

    for test in testcases:
        __check_testcase(test.simulated_input, function, (__stations(), test.start), test.expected_stop)


def test_omroepen_reis():
    function = outputTrip

    case = collections.namedtuple('case', 'start stop expected_start_rank, expected_stop_rank, expected_distance expected_price')
    testcases = [ case("Schagen", "Maastricht", "1e station", "15e station", "14 station", "70 euro"),
                  case("Alkmaar", "Weert", "3e station", "12e station", "9 station", "45 euro"),
                  case("Heerhugowaard", "Sittard", "2e station", "14e station", "12 station", "60 euro") ]


    for test in testcases:
        omroepbericht = function(__stations(), test.start, test.stop)
        assert type(omroepbericht) is str, f"Fout: omroepen_reis({__stations()}, {test.start}, {test.stop}) levert {type(omroepbericht).__name__} ipv string"

        assertmsg = f"Fout: omroepen_reis({__stations()}, {{}}, {{}}) bevat niet de vereiste {{}}-tekst '{{}}'. Jouw returnwaarde: \n<<\n"+omroepbericht+"\n>>"
        assert test.expected_start_rank in omroepbericht, assertmsg.format(test.start, test.stop, 'rangnummer-beginstation', test.expected_start_rank)
        assert test.expected_stop_rank in omroepbericht, assertmsg.format(test.start, test.stop, 'rangnummer-eindstation', test.expected_stop_rank)
        assert test.expected_distance in omroepbericht, assertmsg.format(test.start, test.stop, 'afstand', test.expected_distance)
        assert test.expected_price in omroepbericht, assertmsg.format(test.start, test.stop, 'prijs', test.expected_price)


def __run_tests():
    """ Test alle functies. """
    test_functions = [ test_inlezen_beginstation, test_inlezen_eindstation, test_omroepen_reis ]

    try:
        for test_function in test_functions:
            func_name = test_function.__name__[5:]

            print(f"\n======= Test output '{test_function.__name__}()' =======")
            test_function()
            print(f"Je functie {func_name} werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken!")
        print("Lever je werk nu in op Canvas...")

    except AssertionError as e:
        print(e.args[0])
    except Exception as e:
        print(f"Fout: er ging er iets mis! Python-error: \"{e}\"")
        print(traceback.format_exc())


if __name__ == '__main__':
    module_runner()