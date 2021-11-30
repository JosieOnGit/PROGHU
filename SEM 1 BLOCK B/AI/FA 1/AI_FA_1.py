
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


def primefactors(n):
    num = 2
    factors = []
    while num * num <= n:
        if n % num:
            num += 1
        else:
            n //= num
            factors.append(num)
    if n > 1:
        factors.append(n)
    return sorted(factors)


def gcd(a, b):
    numsa = []
    numsb = []
    for num in div(a):
        numsa.append(num)
    for num in div(b):
        numsb.append(num)
    numsa = numsa[::-1]
    numsb = numsb[::-1]
    for numa in numsa:
        for numb in numsb:
            if numa == numb:
                return numa


def lcm(a, b):
    lcm = (a*b)//gcd(a, b)
    return lcm


def add_frac(n1, d1, n2, d2):
    div = lcm(d1, d2)
    n3 = n1 * (div / d1)
    n4 = n2 * (div / d2)
    num = n3 + n4
    while True:
        if num % 2 == 0 and div % 2 == 0:
            num = num / 2
            div = div / 2
        else:
            break

    return int(num), div
