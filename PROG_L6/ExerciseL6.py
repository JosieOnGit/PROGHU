
# index lst exercise
lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

print(lst[:4])
print(lst[3:6])
print(lst[3:4])
print(lst[-3:-1])
print(lst[3:])
print(lst[-3:])

# string methods exercise
events = '9/13 2:30 PM\n9/14 11:15 AM\n9/14 1:00 PM\n9/15 9:00 AM'
# a
print(events.count("9/14"))
# b
print(events.find("9/14"))
# c
print(events.find("9/15"))
# d
lst = events[13:40].strip().split("\n")
print(lst)
