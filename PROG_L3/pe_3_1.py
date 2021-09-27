# Input verwachte cijfers
cijferPROJA = float(input("Wat voor cijfer verwacht je te halen voor PROJA?: "))
cijferPROG = float(input("Wat voor cijfer verwacht je te halen voor PROG?: "))
cijferMOD = float(input("Wat voor cijfer verwacht je te halen voor MOD?: "))

# Berekening gemiddelde cijfers
gemiddelde = (cijferMOD + cijferPROJA + cijferPROG) / 3

# Berekening beloning van som van cijfers
beloning = (cijferMOD + cijferPROJA + cijferPROG) * 30

# Print eindresultaat
print("Mijn cijfers (gemiddeld een " + str(gemiddelde) + ") leveren een beloning van €" + str(beloning) + " op!")
