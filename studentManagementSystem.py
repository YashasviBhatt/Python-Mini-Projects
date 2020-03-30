# Python Mini Project for Student Management System

from time import sleep

def AddDetails():
    new_record = list()
    print('')
    new_record.append(input('Enter Name : '))
    new_record.append(input('Enter Branch (Available Branches [\'CSE\', \'IT\', \'ECE\', \'EE\', \'ME\']) : ').upper())
    new_record.append(int(input('Enter Year : ')))
    roll_number = input('Enter Roll Number : ')
    if roll_number in roll_list:
        print('Roll Number Can\'t be Same')
        print('Enter Details Again')
        AddDetails()
    else:
        new_record.append(roll_number)
        roll_list.append(roll_number)
    return Verify(new_record)

def Verify(new_record):
    branch_list = ['CSE', 'IT', 'ECE', 'EE', 'ME']
    print('Wait a Moment ...')
    sleep(2)
    if new_record[1] not in branch_list:
        print('Branch Doesn\'t Exist')
        print('Enter Details Again')
        AddDetails()
    else:
        if new_record[2] >= 1 and new_record[2] <= 4:
            student_list.append(new_record)
            print('Data Entered Successfully\n')
        else:
            print('Bachelor of Technology is of Only 4 Years, thus Invalid Year Entered')
            print('Enter Details Again')
            AddDetails()

def RemoveDetails():
    flag = 0
    print('')
    srch_factor = input('Enter either Name or Roll_Number of Student you want to Delete Data of : ')
    for data_index in range(len(student_list)):
        if srch_factor in student_list[data_index]:
            student_list.pop(data_index)
            print('Data Deleted Successfully\n')
            flag = 1
            break
    if flag == 0:
        print('Data not Found')

def ViewDetails():
    print('\nFetching Details ...')
    sleep(2)
    if len(student_list) != 0:
        for data_index in range(len(student_list)):
            print(student_list[data_index])
            sleep(2)
    else:
        print('No Data Exist')
    print('')

def SearchStudent():
    flag = 0
    print('')
    srch_factor = input('Enter either Name or Roll_Number of Student you want to search for : ')
    for data_index in range(len(student_list)):
        if srch_factor in student_list[data_index]:
            print('Data Found')
            print(student_list[data_index])
            print('')
            flag = 1
    if flag == 0:
        print('Data not Found\n')


student_list = list()
roll_list = list()

print('---------------------------------------------------------Student Management System---------------------------------------------------------')
bool_choice = '1'
while bool_choice == '1':
    print('Enter 1 : To View Students Details')
    print('Enter 2 : To Add New Student\'s details')
    print('Enter 3 : To Search a Student\'s Details')
    print('Enter 4 : To Delete Data of a Student')
    choice = input('Enter Choice : ')
    if choice == '1':
        ViewDetails()
    elif choice == '2':
        AddDetails()
    elif choice == '3':
        SearchStudent()
    elif choice == '4':
        RemoveDetails()
    else:
        print('Invalid Choice')
        exit()

    print('Enter 1 : To Continue')
    print('Enter Anything else : To Stop')
    bool_choice = input('Your Choice : ')
    print('')
