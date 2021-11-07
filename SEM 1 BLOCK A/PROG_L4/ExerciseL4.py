# Exercise 1 in class
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(name, ", at age ", age, ", you can vote.", sep="")

else:
    print(name, ", at age ", age, ", you can't vote.", sep="")

# Exercise 2 in class
word = input("Enter a word of your choice: ")

for letter in word:
    print(letter)

# Exercise 2 in class (Alternative)
word = input("Enter a word of your choice: ")

for letter in word:
    if letter in "aeiouijAEIOUIJ":
        print(letter)

# Exercise 3 in class
# A
print()
for i in range(0,11):
    print(i, end=" ")

# B
print()
for i in range(1,10):
    print(i, end=" ")

# C
print()
for i in range(0,10):
    if i % 2 == 0:
        print(i, end=" ")

# D
print()
for i in range(1,10):
    if i % 2 != 0:
        print(i, end=" ")

# E
print()
for i in range(20,70):
    if i % 10 == 0:
        print(i, end=" ")