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
        return self.found
    def num_sum(self):
        if self.calc_sum:
            sum = 0
            for each_number in self.found:
                sum += each_number
        if self.calc_num:
            num = len(self.found)
        return sum, num
class Vowels:
    def __init__(self, user_word):
        self.user_word = user_word.lower()
    def find_vowels(self):
        self.vowels = ['a', 'e', 'i', 'o', 'u']
        self.found = []
        for each_letter in self.user_word:
            if each_letter in self.vowels:
                self.found.append(each_letter)
    def count_vowels(self):
        for each_vowel in self.vowels:
            if each_vowel in self.found:
                print('The number of', each_vowel.upper(), '\'s is', self.found.count(each_vowel))
class Reverser:
    def __init__(self, user_word):
        self.user_word = user_word
    def reverse_string(self):
        return self.user_word[::-1]