# Python Mini-Project for Rock Paper Scissor Game
from random import choice

def Game(score):

    rps = ['ROCK', 'PAPER', 'SCISSOR']
    system_choice = choice(rps)

    user_choice = input('Enter Choice\n{} : '.format(rps)).upper()
    print('')

    if user_choice not in rps:
        print('Invalid Choice')
        Game()

    elif user_choice == system_choice:
        print('Same Choice')
        print('Your Choice : {}\nSystem Choice : {}\n'.format(user_choice, system_choice))

    elif user_choice == 'ROCK':
        if system_choice == 'PAPER':
            print('OOPS You Lose')
            print('Your Choice : {}\nSystem Choice : {}\n'.format(user_choice, system_choice))
            score -= 0.25
        else:
            print('Congrats You Won')
            print('Your Choice : {}\nSystem Choice : {}\n'.format(user_choice, system_choice))
            score += 1

    elif user_choice == 'PAPER':
        if system_choice == 'SCISSOR':
            print('OOPS You Lose')
            print('Your Choice : {}\nSystem Choice : {}\n'.format(user_choice, system_choice))
            score -= 0.25
        else:
            print('Congrats You Won')
            print('Your Choice : {}\nSystem Choice : {}\n'.format(user_choice, system_choice))
            score += 1

    elif user_choice == 'SCISSOR':
        if system_choice == 'ROCK':
            print('OOPS You Lose')
            print('Your Choice : {}\nSystem Choice : {}\n'.format(user_choice, system_choice))
            score -= 0.25
        else:
            print('Congrats You Won')
            print('Your Choice : {}\nSystem Choice : {}\n'.format(user_choice, system_choice))
            score += 1

    return score

score = 0
for trial in range(3):
    score = Game(score)

print('Your Score :', score)