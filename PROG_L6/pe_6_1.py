
def convert(tempC):
    tempF = tempC * 1.8 + 32

    return tempF


def table():
    for degrees in range(-30, 41):
        if degrees % 10 == 0:
            print("{:5} {:7}".format(convert(degrees), float(degrees)))

print("  F       C  ")
table()
