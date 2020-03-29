# The main goal here is to create a sort of “guess the word” game. 
# The user needs to be able to input letter guesses. 
# A limit should also be set on how many guesses they can use. 
# This means you’ll need a way to grab a word to use for guessing. 
# (This can be grabbed from a pre-made list. No need to get too fancy.) 
# You will also need functions to check if the user has actually inputted a single letter, 
# to check if the inputted letter is in the hidden word (and if it is, how many times it appears), 
# to print letters, and a counter variable to limit guesses.
# for each correct guess user will be awarded with 1 point
# for each wrong guess user will be punished with -0.25 points

from random import randint              # randint function is used to generate random numbers

# creating function for game
def Game():
    missing_list = ['so__e_', '_ri_k_t', 'ba_mi_to_', '_oc_ey', '_e__is', '__sket____']  # List from which the problems are to be putted
    answer_list = ['soccer', 'cricket', 'badminton', 'hockey', 'tennis', 'basketball']  # list which contains the answer
    guess_list_ans = [['c', 'r'], ['c', 'e'], ['d', 'n'], ['h', 'k'], ['t', 'n'], ['b', 'a', 'l']]  # list which contains the guess answer
    guess_list = list()                     # list which will be filled with user's guesses

    counter = 10
    score = 0
    flag = 0

    index = randint(0, 5)               # randint function is used to generate random numbers
    print('You only got 10 chances to guess word correctly only one at a time')
    print('For Each Correct Guess Score will be Incremented by 1')
    print('For Each Wrong Guess Score will be Decremented by 0.25')

    print('\nProblem --- Guess the Sport :', missing_list[index])
    print('\n')

    # loop to set the limit of user's guesses
    while counter > 0:
        guess = input('Guess one letter\n')

        if len(guess) == 1:
            if index == 0:
                if guess in guess_list_ans[index]:
                    if guess in guess_list:
                        print('Already Exist')
                    else:
                        print('Correct Guess')
                        score += 1
                        counter -= 1
                        guess_list.append(guess)
                        if len(guess_list) == 2:
                            print('Congratulations You have successfully guessed the word correctly',
                                  answer_list[index])
                            flag = 1
                            exit()
                else:
                    score -= 0.25
                    counter -= 1
                    print('Wrong Guess')

            elif index == 1:
                if guess in guess_list_ans[index]:
                    if guess in guess_list:
                        print('Already Exist')
                    else:
                        print('Correct Guess')
                        score += 1
                        counter -= 1
                        guess_list.append(guess)
                        if len(guess_list) == 2:
                            print('Congratulations You have successfully guessed the word correctly',
                                  answer_list[index])
                            flag = 1
                            exit()
                else:
                    score -= 0.25
                    counter -= 1
                    print('Wrong Guess')

            elif index == 2:
                if guess in guess_list_ans[index]:
                    if guess in guess_list:
                        print('Already Exist')
                    else:
                        print('Correct Guess')
                        score += 1
                        counter -= 1
                        guess_list.append(guess)
                        if len(guess_list) == 2:
                            print('Congratulations You have successfully guessed the word correctly',
                                  answer_list[index])
                            flag = 1
                            exit()
                else:
                    score -= 0.25
                    counter -= 1
                    print('Wrong Guess')

            elif index == 3:
                if guess in guess_list_ans[index]:
                    if guess in guess_list:
                        print('Already Exist')
                    else:
                        print('Correct Guess')
                        score += 1
                        counter -= 1
                        guess_list.append(guess)
                        if len(guess_list) == 2:
                            print('Congratulations You have successfully guessed the word correctly',
                                  answer_list[index])
                            flag = 1
                            exit()
                else:
                    score -= 0.25
                    counter -= 1
                    print('Wrong Guess')

            elif index == 4:
                if guess in guess_list_ans[index]:
                    if guess in guess_list:
                        print('Already Exist')
                    else:
                        print('Correct Guess')
                        score += 1
                        counter -= 1
                        guess_list.append(guess)
                        if len(guess_list) == 2:
                            print('Congratulations You have successfully guessed the word correctly',
                                  answer_list[index])
                            flag = 1
                            exit()
                else:
                    score -= 0.25
                    counter -= 1
                    print('Wrong Guess')

            else:
                if guess in guess_list_ans[index]:
                    if guess in guess_list:
                        print('Already Exist')
                    else:
                        print('Correct Guess')
                        score += 1
                        counter -= 1
                        guess_list.append(guess)
                        if len(guess_list) == 3:
                            print('Congratulations You have successfully guessed the word correctly',
                                  answer_list[index])
                            flag = 1
                            exit()
                else:
                    score -= 0.25
                    counter -= 1
                    print('Wrong Guess')

        else:
            print('Nope Only One Letter at a time')

    if flag == 0:
        print('Oops! You weren\'t too smart to guess the word correctly')

    print('Your Score is', score)

# checking whether wants to keep on playing the game
choice = '1'
while choice == '1':
    Game()          # calling the function
    choice = input('Do You want to Play Again, then Enter 1')
