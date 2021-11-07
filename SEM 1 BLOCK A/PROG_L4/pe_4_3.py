
leeftijd = int(input("Geef je leeftijd: "))
passport = input("Bezit u een Nederlands paspoort? (Ja/Nee): ")

if leeftijd >= 18 and passport == "ja":
    print("Gefeliciteerd, je mag stemmen!")

else:
    print("Helaas, je mag nog niet stemmen!")

