reserved_words = ['quit', 'exit', 'done', 'leave', 'main', 'help']
from time import sleep

# main menu function
def main_menu():
    clear()
    while True:
        # Read main menu text from txt file
        main_menu = open('main_menu.txt', 'r')
        choice = input(main_menu.read() + '\n')
        main_menu.close()
        if choice in ['1', 'play']:
            play()
            break
        elif choice in ['2', 'add word', 'add']:
            add_word()
            break
        elif choice in ['3', 'help']:
            help_user()
            break
        elif choice == '4' or choice in reserved_words[0:4]:
            leave_game()
            break
        else:
            print('Invalid Choice, try again.')
            sleep(1)
            clear()


# play the game
def play():
    clear()
    from random import choice as choose_from
    # Read words and descriptions text from txt files
    words_list = open('words.txt', 'r')
    words = words_list.read().splitlines()
    words_list.close()
    descriptions_list = open('descriptions.txt', 'r')
    descriptions = descriptions_list.read().splitlines()
    descriptions_list.close()
    # Randomly choose a word through index
    chosen_index = choose_from(range(len(words)))
    chosen_word = words[chosen_index]
    chosen_description = descriptions[chosen_index]
    # Variables for the play function
    letter_check = chosen_word.lower()
    letter_check_len = len(letter_check)
    attempts = 8
    user_won = False

    def intro_text():
        print('The word\'s description is:\n' + chosen_description + '\n')
        print('What is the word?\n')
    while True:
        if letter_check_len == len(chosen_word) and attempts == 8:
            intro_text()
        if letter_check_len == 0:
            user_won = True
            break
        user_attempt = input('').lower().replace(' ', '')
        if user_attempt in reserved_words[0:4]:
            leave_game()
        elif len(user_attempt) == 0:
            print('Invalid attempt, try again.')
            sleep(1)
            clear()
        elif len(user_attempt) < len(chosen_word): # check the letters
            for each_letter in user_attempt:
                if each_letter in letter_check:
                    letter_check = letter_check.replace(each_letter, "", 1)
                    letter_check_len -= 1
            clear()
            intro_text()
            print('Letters to go:', letter_check_len, '\n')
            continue
        elif len(user_attempt) >= len(chosen_word): # check the word
            if user_attempt == chosen_word.lower():
                user_won = True
                break
            else:
                if not attempts == 1:
                    attempts -= 1
                    clear()
                    intro_text()
                    print('Attempts to go:', attempts, '\n')
                else:
                    user_won = False
                    break
    # Game outcome
    if user_won:
        print('You Win!!! Congratulations.')
    else:
        print('You lose... Better luck next time.')
    sleep(1)
    main_menu()


# add words
def add_word():
    clear()
    words = open('words.txt', 'a')
    descriptions = open('descriptions.txt', 'a')
    while True:
        print('What word would you like to add?')
        word = input('')
        print('How would you describe that word?')
        desc = input('')
        if word in reserved_words or desc in reserved_words:
            print('\nInvalid input, please try again.\n')
        else:
            break
    if not word == '' and not desc == '':
        words.write(word + '\n')
        descriptions.write(desc + '\n')
        words.close()
        descriptions.close()
        print('\nWord added to the word list!')
    else:
        print('\nNo words added to the list.')
    sleep(1)
    main_menu()


# help function
def help_user():
    clear()
    # Read help text from txt file
    help = open('help.txt', 'r')
    print(help.read())
    help.close()
    # Prompt for user input
    while True:
        user_input = input('')
        if user_input == 'done':
            main_menu()
        elif user_input in reserved_words[0:4]:
            leave_game()
        else:
            print('Invalid input, try again.')
            sleep(1)
            help_user()


# quitting function
def leave_game():
    clear()
    print('\nQuitting...\n')
    sleep(1)
    clear()
    quit()


# Function to clear console
def clear():
    from os import system, name
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


main_menu()
