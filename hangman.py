leave_keywords = ['quit', 'exit', 'done', 'leave']
from time import sleep

# main menu function
def main_menu():
    clear()
    while True:
        print('\nWelcome to Hangman.\nWhat would you like to do?(Pick a number.)\n')
        choice = input('[1] Play\n[2] Add Word\n[3] Help\n[4] Quit\n').lower()
        if choice in ['1', 'play']:
            play()
            break
        elif choice in ['2', 'add word', 'add']:
            add_word()
            break
        elif choice in ['3', 'help']:
            help_user()
            break
        elif choice == '4' or choice in leave_keywords:
            leave_game()
            break
        else:
            print('Invalid Choice, try again.')


# play the game
def play():
    clear()
    from random import choice as choose_from
    words_list = open('hangman_words.txt', 'r')
    words = words_list.read().splitlines()
    global chosen_index
    chosen_index = choose_from(range(len(words)))
    chosen_word = words[chosen_index]
    letter_check = chosen_word.lower()
    letter_check_len = len(letter_check)
    attempts = 8
    user_won = False
    while True:
        if letter_check_len == 0:
            user_won = True
            break
        user_attempt = input('What is the word?\n').lower().replace(' ', '')
        if user_attempt == 'hint':
            hint()
        elif user_attempt in leave_keywords:
            leave_game()
        elif len(user_attempt) == 0:
            print('Invalid attempt, try again.')
        elif len(user_attempt) < len(chosen_word): # check the letters
            for each_letter in user_attempt:
                if each_letter in letter_check:
                    letter_check = letter_check.replace(each_letter, "", 1)
                    letter_check_len -= 1
            print('Letters to go:', letter_check_len)
            continue
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
    if user_won:
        print('You Win!!! Congratulations.')
    else:
        print('You lose. Better luck next time.')
    words_list.close()
    sleep(1)
    main_menu()


# add words
def add_word():
    clear()
    words = open('hangman_words.txt', 'a')
    descriptions = open('hangman_descriptions.txt', 'a')
    while True:
        word = input('What word would you like to add?: \n') + '\n'
        desc = input('What\'s the description for this word?: \n') + '\n'
        if word in leave_keywords or desc in leave_keywords:
            leave_game()
        if len(word) != 0 and len(desc) != 0:
            break
        else:
            print('Invalid input, please try again.')
    words.write(word)
    descriptions.write(desc)
    words.close()
    descriptions.close()
    print('\nWord added to the word list!')
    sleep(1)
    main_menu()

# help function
def help_user():
    clear()
    print('NOTE : The following commands are reserved words that can not be added to the word list.\n')
    print('List of available commands:\n')
    print('To leave the game: quit/exit/done/leave\n')
    print('To ask for a hint: hint\n')
    print('To return to main menu: main\n')
    print('To display this menu: help\n')
    print('Type "done" when you\'re done to return to main menu.')
    while True:
        user_input = input('')
        if user_input == 'done':
            main_menu()
        elif user_input in leave_keywords:
            leave_game()
        else:
            print('Invalid input, try again.')


# quitting function
def leave_game():
    clear()
    print('\nQuitting...\n')
    sleep(1)
    clear()
    quit()


# hint function
def hint():
    descriptions_list = open('hangman_descriptions.txt', 'r')
    descriptions = descriptions_list.read().splitlines()
    chosen_description = descriptions[chosen_index]
    print('The word\'s description is:\n' + chosen_description)
    descriptions_list.close()


# clear function
def clear():
    from os import system, name
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


main_menu()
