
# input uurloon, werkuren
werkuren = float(input("Hoeveel uur werkt u in een week? "))
uurloon = float(input("Wat is uw uurloon? "))

# berekening salaris
salaris = werkuren * uurloon

# output na berekening salaris obv uurloon, werkuren
print(str(werkuren) + " uur werken levert u €" + str(salaris) + " op.")
