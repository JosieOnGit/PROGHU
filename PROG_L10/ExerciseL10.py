
# Scope exercise
def doThing():
    # age = 20
    global age
    print(age)

age = 10
print(age)
doThing()
print(age)
