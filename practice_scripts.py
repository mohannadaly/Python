# IMPORT FUNCTIONS #
from time import sleep
# GENERAL CODE #
answers = ['y', 'yes', 'n', 'no', 'quit', 'exit', 'done', 'leave', 'main', 'help']
# CLASSES DEFINITIONS #
class Calculator:
    def __init__(self, low, high, even_odd, calc_sum, calc_num):
        self.low = low
        self.high = high
        self.even_odd = even_odd
        self.calc_sum = calc_sum
        self.calc_num = calc_num
    def calculate(self):
        self.found = []
        user_range = range(self.low, self.high+1)
        if self.even_odd == 'even':
            for each_number in user_range:
                if each_number % 2 == 0:
                    self.found.append(each_number)
        elif self.even_odd == 'odd':
            for each_number in user_range:
                if each_number % 2 !=0:
                    self.found.append(each_number)
        print('\nThe', self.even_odd, 'numbers are:', self.found)
        if self.calc_sum:
            sum = 0
            for each_number in self.found:
                sum += each_number
            print('\nThe sum of', self.even_odd, 'numbers is:', sum)
        if self.calc_num:
            print('\nThe number of', self.even_odd, 'numbers is:', len(self.found))
class Vowels:
    def __init__(self, user_word):
        self.user_word = user_word.lower()
    def find_vowels(self):
        self.vowels = ['a', 'e', 'i', 'o', 'u']
        self.found = []
        for each_letter in self.user_word:
            if each_letter in self.vowels:
                self.found.append(each_letter)
        return self.found
    def count_vowels(self):
        for each_vowel in self.vowels:
            if each_vowel in self.found:
                print('The number of', each_vowel.upper() + '\'s is', self.found.count(each_vowel))
class Reverser:
    def __init__(self, user_word):
        self.user_word = user_word
    def reverse_string(self):
        return self.user_word[::-1]
# SUB-CLASSES DEFINITIONS #
class RangeError(Exception):
    pass
class ExitWords(Exception):
    pass
class AnsErr(Exception):
    pass
class ans_main(Exception):
    pass
class ans_help(Exception):
    pass
# SUB-FUNCTIONS DEFINITIONS #
def clear(time):
    sleep(time)
    from os import system, name
    if name == 'nt':
        system('cls')
    else:
        system('clear')
def read_file(file_name, begin, end):
    file = open(file_name + '.txt', 'r')
    text_list = file.read().splitlines()
    file.close()
    if end == 0:
        end = len(text_list)
    for i in range(begin - 1, end):
        print(text_list[i] + '\n')
def leave_script():
    clear(0)
    print('\nQuitting...\n')
    clear(1)
    quit()
def ans_check(var):
    if var in answers[4:8]:
        raise ExitWords
    elif var == answers[8]:
        raise ans_main
    elif var == answers[9]:
        raise ans_help
def return_prompt():
    while True:
            user_input = input('\nType "main" to return to the main menu...\n\n')
            if user_input == 'main':
                main_menu()
            elif user_input in answers[4:8]:
                leave_script()
            else:
                print('\nInvalid input, please try again...')
# MAIN FUNCTIONS DEFINITIONS #
def main_menu():
    while True:
        clear(0)
        read_file('master_text', 1, 7)
        choice = input('')
        if choice in ['1', 'calculator']:
            calculator()
            break
        elif choice in ['2', 'vowels']:
            vowels()
            break
        elif choice in ['3', 'reverser']:
            reverser()
            break
        elif choice in ['4', 'help']:
            help()
            break
        elif choice in ['5', 'quit', 'leave', 'exit', 'done']:
            leave_script()
            break
        else:
            print('Invalid choice, please try again...')
            sleep(1.5)
def calculator():
    clear(0)
    while True:
        try:
            low = round(float(input("What's the lower limit to your range?: ")))
            high = round(float(input("What's the higher limit to your range?: ")))
            if low > high: raise RangeError
            num = input('Would you like to count the even/odd numbers?: ')
            ans_check(num)
            if num not in answers: raise AnsErr
            sums = input('Would you like to calculate the same of the even/odd numbers?: ')
            ans_check(sums)
            if sums not in answers: raise AnsErr
            break
        except ValueError:
            print('Invalid input, please try again...')
            clear(1.5)
        except RangeError:
            print('Invalid range, please try again...')
            clear(1.5)
        except ExitWords:
            leave_script()
        except ans_main:
            main_menu()
        except ans_help:
            help()
        except AnsErr:
            print('Invalid answer, please try again...')
            clear(1.5)
    if num in answers[0:2]: num = True
    else: num = False
    if sums in answers[0:2]: sums = True
    else: sums = False
    even = Calculator(low, high, 'even', sums, num)
    odd = Calculator(low, high, 'odd', sums, num)
    clear(0)
    even.calculate()
    odd.calculate()
    return_prompt()
def vowels():
    clear(0)
    while True:
        try:
            user_word = input('Enter your word: ').lower()
            if user_word == '': raise AnsErr
            ans_check(user_word)
            break
        except ExitWords:
            leave_script()
        except ans_main:
            main_menu()
        except ans_help:
            help()
        except AnsErr:
            print('Invalid answer, please try again...')
            clear(1.5)
    vowel = Vowels(user_word)
    clear(0)
    x = vowel.find_vowels()
    print('Found the following vowels: \n')
    print(list(set(x)))
    print('')
    vowel.count_vowels()
    return_prompt()
def reverser():
    clear(0)
    while True:
        try:
            user_string = input('Enter your string: ')
            if user_string == '': raise AnsErr
            ans_check(user_string)
            break
        except ExitWords:
            leave_script()
        except ans_main:
            main_menu()
        except ans_help:
            help()
        except AnsErr:
            print('Invalid answer, please try again...')
            clear(1.5)
    clear(0)
    print('Your reversed string is:', user_string[::-1])
    return_prompt()
def help():
    while True:
        clear(0)
        read_file('master_text', 8, 13)
        return_prompt()
main_menu()
