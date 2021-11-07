
# Acronym Exercise
def acronym(sentence):
    lst = sentence.split(sep=" ")
    acronym = ""
    for letter in lst:
        acronym += letter[0].upper()
    return acronym


sentence = input("Please fill in a sentence: ")
print(acronym(sentence))
