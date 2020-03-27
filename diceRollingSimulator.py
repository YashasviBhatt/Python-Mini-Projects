# Like the title suggests,
# this project involves writing a program that simulates rolling dice.
# When the program runs, it will randomly choose a number between 1 and 6.
# (Or whatever other integer you prefer — the number of sides on the die is up to you.)
# The program will print what that number is.
# It should then ask you if you’d like to roll again.
# For this project, you’ll need to set the min and max number that your dice can produce.
# For the average die, that means a minimum of 1 and a maximum of 6.
# You’ll also want a function that randomly grabs a number within that range and prints it.

from random import randint          # used to generate random integer from the given range

history = list()

flag = '1'
while flag == '1':
    output = randint(1,6)
    history.append(output)
    print(output,'\n')
    flag = input('1. Enter 1 to Roll Again\n')
    if flag != '1':
        print('\nThank You for Using this Dice')

print('Your History\n',history)