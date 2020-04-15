def Swap(num1, num2):
    temp = num1
    num1 = num2
    num2 = temp
    return num1, num2

number_of_students = int(input('Enter Number of Students : '))
student_list = list()

print('\nEnter Name and Marks of Student\n')

for student in range(number_of_students):
    student_detail = list()
    student_detail.append(input('Enter Name : '))
    student_detail.append(int(input('Enter Marks : ')))
    student_list.append(student_detail)
    print()

for lst_ptr1 in range(len(student_list)):
    for lst_ptr2 in range(len(student_list)-lst_ptr1-1):
        if student_list[lst_ptr2][1] < student_list[lst_ptr2 + 1][1]:
            student_list[lst_ptr2], student_list[lst_ptr2 + 1] = Swap(student_list[lst_ptr2], student_list[lst_ptr2 + 1])

top = int(input('Enter the Number of Top Students Details you want to see : '))
for data in range(top):
    print(student_list[data])