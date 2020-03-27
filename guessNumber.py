# This project uses the random module in Python.
# The program will first randomly generate a number unknown to the user.
# The user needs to guess what that number is.
# (In other words, the user needs to be able to input information)
# If the user’s guess is wrong,
# the program should return some sort of indication as to how wrong (e.g. The number is too high or too low).
# If the user guesses correctly, a positive indication should appear.
# You’ll need functions to check if the user input is an actual number,
# to see the difference between the inputted number and the randomly generated numbers,
# and to then compare the numbers.

from random import randint          # used to generate random integer from the given range

random_var = randint(1,10)

counter = 0
flag = 0

print('Enter Value Between 1-10')

while counter <= 5:
    counter+=1
    test_var = int(input('Guess the Number\n'))
    if test_var <= random_var - 5 or test_var >= random_var + 5:
        print('Predicted Value is very far to be Correct, Try Again')
    elif test_var < random_var - 3 or test_var > random_var + 3:
        print('Not Correct, Try Again')
    elif test_var < random_var - 1 or test_var > random_var + 1:
        print('Close But Not Correct, Try Again')
    elif test_var == random_var - 1 or test_var == random_var + 1:
        print('Oops, you almost predicted Correctly, Try Again')
    elif test_var == random_var:
        print('Correctly Predicted in {} try'.format(counter))
        flag += 1
        exit()

print('Oh! no, all tries are over')
print('Correct Nummber was',random_var)