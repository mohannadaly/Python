while True:
    word = input("\nString: ")
    if len(word) != 0:
        print("\nReversed string: " + word[::-1])
        break
    else:
        print("\nInvalid input.")