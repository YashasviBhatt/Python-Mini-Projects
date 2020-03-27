# The program will first prompt the user for a series of inputs a la Mad Libs.
# For example, a singular noun, an adjective, etc.
# Then, once all the information has been inputted,
# the program will take that data and place them into a premade story template.
# You’ll need prompts for user input,
# and to then print out the full story at the end with the input included.

name = input('Enter Name : ')
city = input('Enter City Name : ')
occupation = input('Enter Your Occupation : ')
organisation = input('Enter Name of your Organization : ')
study = input('Enter your Max Study Level : ')

print('Entered Details are as follows : ')
print('Your Name is '+name)
print('Your City of Living is '+city)
print('You Occupation is '+occupation+' at '+organisation)
print('You have Completed '+study)