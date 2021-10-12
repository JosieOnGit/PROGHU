
valueError = False
while not valueError:
    try:
        # input wage, hours
        hours = float(input("How many hours do you work in a week? "))
        wage = float(input("What is your hourly wage? "))

        # calculating the salary
        salary = hours * wage

        # printing the output after calculating the salary
        print(f"Working for {hours} hours gives you €{salary}.")
        break
    except ValueError:
        print("Numbers only!!!!!!!!")
