# Choose a word and associate it to its descrption.
from random import choice as choose_from
from time import sleep
words = open('hangman_words.txt', 'r').read().splitlines()
descriptions = open('hangman_descriptions.txt', 'r').read().splitlines()
chosen_index = choose_from(range(len(words)))
chosen_word = words[chosen_index]
chosen_description = descriptions[chosen_index]
letter_check = chosen_word.lower()
letter_check_len = len(letter_check)
attempts = 8
user_won = False
# core code of the game
print('Available attempts:', attempts)
while True:
    if letter_check_len == 0:
        user_won = True
        break
    user_attempt = input('What is the word?\n').lower().replace(' ', '')
    if user_attempt.lower() in ['quit', 'exit', 'done']: # quit check
        print('Quitting...')
        sleep(1)
        quit()
    elif user_attempt.lower() in ['hint', 'help']:
        print(chosen_description)
    elif user_attempt == '':
        print('Invalid attempt, try again.')
    elif len(user_attempt) < len(chosen_word): # check the letters
        for each_letter in user_attempt:
            if each_letter in letter_check:
                letter_check = letter_check.replace(each_letter, "", 1)
                letter_check_len -= 1
        print('Letters to go:', letter_check_len)
    elif len(user_attempt) >= len(chosen_word): # check the word
        if user_attempt == chosen_word.lower():
            user_won = True
            break
        else:
            if not attempts == 1:
                attempts -= 1
                print('Attempts to go:', attempts)
            else:
                user_won = False
                break
# outcome of the game
if user_won:
    print('You Win!!! Congratulations.')
else:
    print('You lose. Better luck next time.')
