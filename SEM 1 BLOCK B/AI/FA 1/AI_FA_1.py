
def isEven(num):
    # Divide by 2, if the remainder is 0, num is even. If there's a remainder, num is uneven
    if num % 2 == 0:
        return True
    else:
        return False


def floor(real):
    floor = int(real // 1)
    return floor


def ceil(real):
    ceil = int(-1 * real // 1 * -1)
    return ceil


def div(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)

    return sorted(divisors)


def isPrime(num):
    divisors = div(num)
    if len(divisors) > 2 or len(divisors) == 1:
        return False
    else:
        return True


def primes(num):
    primelist = []
    for number in range(1, num + 1):
        if isPrime(number):
            primelist.append(number)

    return sorted(primelist)


num = int(input("Insert a number >> "))  # Basic num input
real = input("Insert a number with decimals >> ")  # Basic real input
print(primes(num))
