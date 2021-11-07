
num2 = 0
for table in range(1, 11):
    num1 = 0
    num2 += 1
    for sum in range(1, 11):
        calc = sum * table
        num1 += 1
        print(f"{num1} * {num2} = {calc}")
