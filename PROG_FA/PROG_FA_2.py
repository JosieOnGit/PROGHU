
def standaardprijs(afstandKM):
    price = afstandKM * 0.80
    if afstandKM <= 0:
        price = 0

    elif afstandKM > 50:
        price = 15 + (afstandKM * 0.60)

    else:
        price = afstandKM * 0.80

    return round(price, 2)


afstandKM = int(input("Input nummer"))
standaardprijs(afstandKM)


def ritprijs(leeftijd, weekendrit, afstandKM):
    """
    Het eerste wat deze functie moet doen, is het aanroepen van
    functie standaardprijs, waarbij de afstand in kilometers doorgegeven
    moet worden om de standaardprijs voor de rit op te vragen.
    Aan de hand van de standaardprijs kan de actuele ritprijs worden berekend.
    De regels zijn als volgt:
     * Op werkdagen reizen kinderen (onder 12 jaar) en ouderen (65 en ouder) met 30% korting.
     * In het weekend reist deze groep met 35% korting.
     * Overige leeftijdsgroepen betalen de gewone prijs, behalve in het weekend. Dan reist
       deze leeftijdsgroep met 40% korting.
    Args:
        leeftijd (int): De leeftijd van de reiziger in gehele jaren.
        weekendrit (bool): True als het een rit in het weekend betreft, anders False.
        afstandKM (int): De reisafstand in kilometers.
    Returns:
        float: De berekende ritprijs.
    """
    return
