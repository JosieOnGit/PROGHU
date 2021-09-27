
def standaardprijs(afstandKM):
    """
    Bepaal de prijs van een treinrit. Iedere treinrit kost 80 cent per kilometer,
    maar als de rit langer is dan 50 kilometer betaal je een vast bedrag van €15,-
    plus 60 cent per kilometer.
    Ga bij invoer van negatieve afstanden uit van een afstand van
    0 kilometer (prijs is dan dus 0 Euro).
    Args:
        afstandKM (int): De reisafstand in kilometers.
    Returns:
        float: De berekende standaardprijs.
    """
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

# This next line will appear on P4 soon


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
