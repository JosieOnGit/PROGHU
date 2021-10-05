
def season(month):
    if 3 <= month <= 5:
        print("It's Spring.")
    elif 6 <= month <= 8:
        print("It's Summer.")
    elif 9 <= month <= 11:
        print("It's Autumn.")
    elif month == "12" or 0 < month <= 2:
        print("It's Winter.")
    elif 0 >= month <= 13:
        print("Invalid input.")
    else:
        print("Please input numbers only.")


month = int(input("Which month (mm) is it? Please input numbers only. "))
season(month)
