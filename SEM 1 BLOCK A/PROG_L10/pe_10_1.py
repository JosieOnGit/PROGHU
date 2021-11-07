
import json

with open("stations.json", "r") as jsonFile:
    data = json.load(jsonFile)
    payload = data["payload"]

for station in payload:
    names = station["namen"]
    nameLong = names["lang"]
    code = station["code"]
    stationType = station["stationType"]
    print(f"{nameLong:23} - {code:5} : {stationType}")

lst = []
for station in payload:
    item = station["lng"]
    lst.append(item)
for station in payload:
    if max(lst) == station["lng"]:
        eastStation = station["namen"]["lang"]

print(f"\nThe station furthest to the east is {eastStation}")
