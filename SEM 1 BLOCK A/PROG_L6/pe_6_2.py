
def prettyprint():
    file = open("pe_6_2_cardnumbers.txt")
    content = file.readlines()
    for line in content:
        contentdef = line.strip().split(sep=", ")
        print(contentdef[1], "has card number:", contentdef[0])
    file.close()


prettyprint()
