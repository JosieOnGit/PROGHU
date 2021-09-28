
def prettyprint():
    file = open("pe_6_2_cardnumbers.txt")
    content = file.readlines()
    for lines in content:
        contentdef = lines.strip().split(sep=", ")
        print(contentdef[1], "has card number:", contentdef[0])
        return contentdef


prettyprint()
