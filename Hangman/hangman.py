from time import sleep
reserved_words = ['main', 'help']
exit_words = ['quit', 'exit', 'leave']
# main menu function
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
    dic = words_dic()
    chosen_word = choose_from(list(dic))
    chosen_desc = dic[chosen_word]
    letter_check = chosen_word.lower()
    letter_check_len = len(letter_check)
    attempts = 8
    user_won = False
    def intro_text():
        print('The word\'s description is:\n' + chosen_desc + '\n')
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
        print('\nYou Win!!! Congratulations.')
    else:
        print('You lose... Better luck next time.')
    sleep(1)
    main_menu()
# add words
def add_word():
    clear(0)
    words_list = list(words_dic())
    while True:
        word = input('What word would you like to add?\n').lower().replace(' ', '')
        if word in exit_words:
            leave_game()
        elif word in reserved_words or word in words_list:
            print('Word already exists or is a reserved word, try again...')
            clear(1.5)
            continue
        elif word == '':
            print('No words added!')
            clear(1.5)
            break
        desc = input('How would you describe that word?\n')
        if desc in exit_words:
            leave_game()
        elif desc == '':
            print('Invalid description, try again...')
            clear(1.5)
            continue
        words_file = open('words.txt', 'r+')
        words_file.read()
        words_file.write(word + ':' + desc + '\n')
        words_file.close()
        clear(0)
        print('Added word succuessfully!')
        sleep(1.5)
        break
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
    if file_name not in ['words']:
        for i in range(begin - 1, end):
            print(text_list[i] + '\n')
    else:
        return text_list
# turn the words.txt file into a dictionary
def words_dic():
    words_file = open('words.txt', 'r')
    dic = {}
    for each_item in words_file.read().splitlines():
        colon = each_item.index(':')
        dic[each_item[:colon]] = each_item[colon+1:]
    words_file.close()
    return dic
# clear console
def clear(time):
    sleep(time)
    from os import system, name
    if name == 'nt':
        system('cls')
    else:
        system('clear')
main_menu()
