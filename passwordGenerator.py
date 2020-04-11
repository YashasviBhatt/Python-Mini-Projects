# Python Mini-Project of Password Generator
from datetime import datetime

# method which will generate the password
def passwordGenerator(name, year_of_birth, choice_special_characters, choice_add_more):
    new_name = ''
    for index in range(len(name)):
        if name[index] != ' ':
            if name[index-1] == ' ':
                new_name = new_name + name[index].upper()
            else:
                new_name = new_name + name[index].lower()

    if choice_special_characters == 'y':
        password = new_name + '@' + year_of_birth
    else:
        password = new_name + year_of_birth

    if choice_add_more == 'y':
        more_details = input('Enter Detail you want to add more : ')
        details = ''
        for index in range(len(more_details)):
            if more_details[index] != ' ':
                if more_details[index - 1] == ' ':
                    details = details + more_details[index].upper()
                else:
                    details = details + more_details[index].lower()
        password = password + '.' + details

    return password

# Main method which will start the program
def Main():
    choice_numbers = input('Do you want to add Numbers in your Password (y/n) : ')
    choice_special_characters = input('Do you want to add Special Characters in your Password (y/n) : ')

    name = input('Enter Your Full Name : ')
    year_of_birth = ''

    if choice_numbers == 'y':
        year_of_birth = input('Enter Your Year of Birth : ')
        if int(year_of_birth) > (datetime.now().year - 60) and int(year_of_birth) < (datetime.now().year - 20):   #datetime.now().year will return system's current year
            pass
        else:
            print('Invalid Year of Birth Entered, Enter Details Again')
            Main()
            exit()

    choice_add_more = input('Do you want to add Something More in your Password (y/n) : ')
    password = passwordGenerator(name, year_of_birth, choice_special_characters, choice_add_more)

    print('\nGenerated Password :', password)

# calling Main() method
Main()