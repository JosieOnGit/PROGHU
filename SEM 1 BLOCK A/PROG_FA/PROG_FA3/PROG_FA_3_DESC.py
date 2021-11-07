'''
Het gehele programma bevindt zich in een constante loop, deze loop print constant een lijst met opties van 1 tot en met 5
Elke optie heeft een bijbehorende functie, en na het printen van de opties wordt de gebruiker gevraagd een nummer in te voeren

Wanneer de gebruiker "1" invoert:
    functie freeLockersCount() wordt gebruikt.
    Deze functie bekijkt de lijst met lockers en telt het aantal regels.
    Het aantal vrije lockers is (12 - aantal regels)
    Deze hoeveelheid wordt gereturned en later uitgeprint.

Wanneer de gebruiker "2" invoert:
    functie newLocker() wordt gebruikt.
    Deze functie bekijkt het bestand en zoekt naar nummers van 1 tot en met 12
    Als het nummer al in gebruik is, dan kan de kluis niet opnieuw geclaimed worden, en loopt het programma door
        Tenzij alle nummers al in gebruik zijn, dan breekt het programma af en wordt er een foutmelding geprint (-2)
    Als er een nummer in de range is die niet in gebruik is, gaat het programma door en moet de gebruiker een wachtwoord aanmaken
    Als het wachtwoord korter is dan 4 tekens en/of een ";" bevat, dan breekt de functie af, en wordt er een foutmelding geprint (-1)
    Zo niet, dan wordt de regel ge-append aan het bestand, en eindigt de functie


Wanneer de gebruiker "3" invoert:
    functie openLocker() wordt gebruikt.
    Deze functie bekijkt het bestand met alle kluizen en wachtwoorden.
    Vervolgens vraagt het programma de gebruiker om hun kluisnummer, en bekijkt het het bestand om te zien of deze kluis in gebruik is
    Zo niet? Dan breekt de functie af en returnt het False.
    Zo wel? Dan wordt de gebruiker gevraagd hun wachtwoord in te voeren.
    De functie bekijkt dan of er een regel is die overeenkomt met de combinatie van kluisnummer;wachtwoord.
    Zo niet? Dan breekt de functie af en returnt het False.
    Zo wel? Dan returnt de functie True.

Wanneer de gebruiker "4" invoert:
    functie returnLocker wordt gebruikt:
    Deze functie bekijkt ook het bestand met alle kluizen en wachtwoorden.
    Het programma vraagt weer om het kluisnummer en wachtwoord, maar opent deze kluis niet.
    De functie clear() schrijft het bestand over met een "", het leegt het bestand dus.
    Elke regel die niet overeenkomt met de combinatie van kluisnummer;wachtwoord, wordt opnieuw ge-append aan het bestand.
    Als de combinatie correct is, dus de regel bestaat al in het bestand, dan wordt deze niet opnieuw ge-append.
    Als deze flow goed verloopt, returnt het programma True.
    Zodra er een fout optreedt, zoals een verkeerde combinatie van kluisnummer;wachtwoord, of een kluis die niet in gebruik is, dan returnt het programma False.

Wanneer de gebruiker "5" invoert:
    Het programma stopt per direct met quit()

Wanneer de gebruiker een andere input geeft:
    Er wordt een foutmelding gegeven, het programma herhaalt.
'''