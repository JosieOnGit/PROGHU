
def tickersToDict():
    file = open("tickers.txt")
    tickerDict = {}
    for line in file.readlines():
        tickerLine = line.strip().split(sep=":")
        tickerDict[tickerLine[0]] = tickerLine[1]
    return tickerDict


def nameToSymbol(name, tickers):
    checkName = name.upper()
    return tickers[checkName]


def symbolToName(symbol, tickers):
    for companyName in tickers.keys():
        if tickers[companyName] == symbol:
            return companyName


tickers = tickersToDict()
name = input("Enter company name!!: ")
print(f"Ticker symbol!!: {nameToSymbol(name, tickers)}!!!!!!!")

symbol = input("Enter company symbol!!: ")
print(f"Ticker name!!: {symbolToName(symbol, tickers)}!!!!!!!")
