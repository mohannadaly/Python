# Choose a word and associate it to its descrption.
from random import choice as choose_from
words = open('hangman_words.txt', 'r').read().splitlines()
descriptions = open('hangman_descriptions.txt', 'r').read().splitlines()
chosen_index = choose_from(range(len(words)))
chosen_word = words[chosen_index]
chosen_description = descriptions[chosen_index]
attempts = 8
print('Available attempts:', attempts)
while True:
    user_attempt = input('What is the word?\n').lower()
    if user_attempt == chosen_word.lower():
        print('The word is', chosen_word)
        print('You Win!!! Congratulations.')
        break
    elif user_attempt in chosen_word.lower():

    elif user_attempt == '':
        print('Invalid attempt, try again.')
    else:
        attempts -= 1
        if attempts > 0:
            print('Wrong! Try again.')
            print('Available attempts:', attempts)
        else:
            print('You lose! Better luck next time.')
            break
