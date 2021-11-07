
while True:
    wordInput = input("Please insert a word with four letters: ")
    if len(wordInput) == 4:
        print(f"{wordInput} has {len(wordInput)} letters. Success.")
        break
    print(f"{wordInput} has {len(wordInput)} letters. Please try again.")
