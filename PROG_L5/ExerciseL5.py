
# în class
def kwadrateer(grondtal):
    resultaat = grondtal ** 2
    print(resultaat)


kwadrateer(4)

# In-class exercise hello()
def hello(name):
    print("Hello,", name + ", to the world of Python!")

name = input("What's your name? ")
hello(name)


# In-class exercise rng()

def rng(lst):
    # lst = [getal1, getal2, getal3, getal4]
    res = max(lst) - min(lst)
    print(res)
    return res


rng([12, 4, 9, -4, 8])
