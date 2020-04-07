# Python Mini-Project for Words Typing Speed Calculator

import time                     # time library contains the function which are related to time operation
from random import randint      # randint generate random int value from the given range

print('Enter following text to check your typing speed')

# creating a random list which contains various sentences
text_list = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit',
             'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua',
             'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris',
             'nisi ut aliquip ex ea commodo consequat, Duis aute irure dolor in',
             'reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur']

text = text_list[randint(1, len(text_list))]        # using this one can't copy the text and increase the word typing speed

# \033[1m is used to bold the character and \033[0m is used to change back to normal
print('\033[1m' + '\"{}\"'.format(text) + '\033[0m')

start = time.time()             # calculate the current time of the system
input_text = input()
end = time.time()               # calculate the current time of the system
total_time = end-start          # calculating the time duration in which the sentence was written

words = 1

for letter in text:
    if letter == ' ':
        words += 1

if input_text == text :
    print('Your Speed was\n', int((words/total_time)*60), ' words/minute')
else :
    print('Input Text does not match the Actual Text')