
def kwadratensom(getallen):
    posnum = []
    facnum = []
    for getal in getallen:
        if getal >= 0:
            posnum.append(getal)
    for getal in posnum:
        factornum = getal ** 2
        facnum.append(factornum)
    result = facnum[0] + facnum[1] + facnum[2] + facnum[3]
    print(result)


getallen = [1, 2, 3, 4, -4, -6]
kwadratensom(getallen)
