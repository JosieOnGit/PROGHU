
def hoogvliegers(dict_studenten_cijfers):
    new_dict = {}
    for name, grade in dict_studenten_cijfers.items():
        if float(grade) > 9.0:
            new_dict[name] = grade
    return new_dict


dict_studenten_cijfers = {
    "Martijn van Egmond" : 5.6,
    "Willem Driebergen" : 8.6,
    "Achmed El-Assouam" : 9.3,
    "Annette Appolodor" : 9.0,
    "Kágos Núje" : 7.9,
    "Iosifin Álusken" : 9.6,
    "Maxim Chlebowska" : 6.7
}

print(hoogvliegers(dict_studenten_cijfers))
