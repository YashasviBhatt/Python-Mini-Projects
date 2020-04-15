# Program for Number (with base in range between 2 and 36) Conversion to Decimal

# Method for Value Converter
def Converter(input_number, base):
    converted_number = 0

    if type(input_number) == int:
        power = 0
        for digit in str(input_number):
            if 0 <= int(digit) < base:
                converted_number = converted_number + (int(digit) * (base**power))
                power += 1
            else:
                print('Invalid Value according to base', base)
                print('Please Enter Again\n')
                Main()
                exit()
    else:
        number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        power = 0
        for digit in input_number:
            if digit in number_list:
                converted_number = converted_number + (int(digit) * (base ** power))
                power += 1
            elif (ord(digit) - 87) <= base:
                converted_number = converted_number + ((ord(digit) - 87) * (base ** power))
                power += 1
            else:
                print('Invalid Value according to base', base)
                print('Please Enter Again\n')
                Main()
                exit()


    return converted_number

# Function which will call other functions
def Main():
    base = int(input('Enter Base (in range 2 and 36) : '))
    if 2 <= base <= 36:
        if base > 10:
            print('\nEnter\nA for 10\nB for 11\nC for 12\nand so on ...\n')
            input_number = input('Enter Number : ')[::-1].lower()
            print()
        else:
            input_value = input('Enter Number : ')[::-1]            # [::-1] is used to reverse the string
            input_number = int(input_value)
            print()
    else:
        print('Invalid Base for this Program')
        print('Please Enter Again\n')
        Main()
        exit()

    converted_number = Converter(input_number, base)

    print('The Converted Decimal Equivalent is : {}'.format(converted_number))
    return True

# Calling Main()
Main()
