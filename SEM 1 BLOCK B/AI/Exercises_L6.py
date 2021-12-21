
def multiply(x, y):
    if x == 1:
        return y
    return y + multiply(x-1, y)


print(multiply(4, 3))


def faculty(num):
    result = 1
    if num == 0:
        return result
    for item in range(1, num + 1):
        result = result * item
    return result


# num = int(input("Input a number >> "))
# print(faculty(num))


def exponent(exp):
    if exp == 1:
        return exp * 2
    return 2 * exponent(exp-1)


def baseExponent(base, exp):
    if base == 1:
        return exp
    return exp * (baseExponent(base - 1, exp))


exp = int(input("Input an exponent >> "))
base = int(input("Input a base number >> "))
print(exponent(exp))
print(baseExponent(base, exp))
