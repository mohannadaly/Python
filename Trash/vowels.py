vowels, found = (['a', 'e', 'i', 'o', 'u'],[])
while True:
    word = input("Word: ")
    if word in ['quit', 'exit', 'done']:
        quit()
    elif len(word) > 0:
        break
    else:
        print("\nPlease enter a word.\n")
for letter in word.lower():
    if letter in vowels:
        found.append(letter)
if len(found) == 0:
    print("\nNo vowels found.")
else:
    print("\nThe number of vowels is", len(found), "\n")
    for letters in vowels:
        if letters in found:
            print("The number of", letters.upper() + "\'s is", str(found.count(letters)))
