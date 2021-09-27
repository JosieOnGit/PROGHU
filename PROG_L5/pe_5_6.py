
def edit(list):
    list.pop()
    list.pop()
    list.pop()
    list.append("d")
    list.append("e")
    list.append("f")


list = ["a", "b", "c"]
print(list)
edit(list)
print(list)
