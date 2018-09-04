from time import sleep
reserved_words = ['main', 'help']
exit_words = ['quit', 'exit', 'leave']
def main_menu():
    clear(0)
    while True:
        read_file('master_text', 1, 6)
        choice = input('')
        if choice in ['1', 'play']:
            play()
            break
        elif choice in ['2', 'add word', 'add']:
            add_word()
            break
        elif choice in ['3', 'help']:
            help_user()
            break
        elif choice == '4' or choice in exit_words:
            leave_game()
            break
        else:
            print('Invalid Choice, try again.')
            clear(1)
# play the game
def play():
    clear(0)
    from random import choice as choose_from
    words = read_file('words', 0, 0)
    descriptions = read_file('descriptions', 0, 0)
    # choose a random index
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
        if user_attempt in exit_words:
            leave_game()
        elif user_attempt == 'main':
            main_menu()
        elif user_attempt == '':
            print('Invalid attempt, try again.')
            clear(1)
        elif len(user_attempt) < round((len(chosen_word)/2) + 1):
            for each_letter in user_attempt:
                if each_letter in letter_check:
                    letter_check = letter_check.replace(each_letter, "", 1)
                    letter_check_len -= 1
            clear(0)
            intro_text()
            print('Letters to go:', letter_check_len, '\n')
            continue
        elif len(user_attempt) >= round((len(chosen_word)/2) + 1):
            if user_attempt == chosen_word.lower():
                user_won = True
                break
            else:
                if not attempts == 1:
                    attempts -= 1
                    clear(0)
                    intro_text()
                    print('Attempts to go:', attempts, '\n')
                else:
                    user_won = False
                    break
    if user_won:
        print('You Win!!! Congratulations.')
    else:
        print('You lose... Better luck next time.')
    sleep(1)
    main_menu()
# add words
def add_word():
    clear(0)
    words = open('words.txt', 'r+')
    words_list = [x.lower() for x in words.read().splitlines()]
    descriptions = open('descriptions.txt', 'a')
    while True:
        written = 0
        print('What word would you like to add?')
        word = input('')
        if word == '':
            print('\nNo words added to the list.')
            sleep(1)
            break
        elif word in exit_words:
            leave_game()
        elif ' ' in word:
            print('Words can\'t contain spaces, please try again...')
            clear(1.5)
            continue
        elif word.lower() in reserved_words or word.lower() in words_list:
            print('\nWord already exists or is a reserved word, please try again...\n')
            clear(1.5)
            continue
        else:
            written += 1
        print('How would you describe that word?')
        desc = input('')
        if desc == '':
            print('Invalid description, please try again.')
            clear(1.5)
            continue
        elif desc in exit_words:
            leave_game()
        else:
            written += 1
        words.write(word + '\n')
        descriptions.write(desc + '\n')
        break
    if written == 2:
        clear(0)
        print('Word added!')
        sleep(1)
    words.close()
    descriptions.close()
    main_menu()
# help function
def help_user():
    clear(0)
    read_file('master_text', 7, 12)
    while True:
        user_input = input('')
        if user_input == 'main':
            main_menu()
        elif user_input in exit_words:
            leave_game()
        else:
            print('Invalid input, try again.')
            sleep(1)
            help_user()
# quitting function
def leave_game():
    clear(0)
    print('\nQuitting...\n')
    clear(1)
    quit()
# assign text from files to variables
def read_file(file_name, begin, end):
    file = open(file_name + '.txt', 'r')
    text_list = file.read().splitlines()
    file.close()
    if end == 0:
        end = len(text_list)
    if file_name not in ['words', 'descriptions']:
        for i in range(begin - 1, end):
            print(text_list[i] + '\n')
    else:
        return text_list
# clear console
def clear(time):
    sleep(time)
    from os import system, name
    if name == 'nt':
        system('cls')
    else:
        system('clear')
main_menu()