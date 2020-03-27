# Remember Adventure? Well, we’re going to build a more basic version of that.
# A complete text game, the program will let users move through rooms based on user input and get descriptions of each room.
# To create this, you’ll need to establish the directions in which the user can move,
# a way to track how far the user has moved (and therefore which room he/she is in),
# and to print out a description.
# You’ll also need to set limits for how far the user can move.
# In other words, create “walls” around the rooms that tell the user,
# “You can’t move further in this direction.”

# Function to move between rooms
def RoomAdventure(room_num, room_history):
    flag = 0
    print('You have Entered in Room',room_num)
    for room_choice in rooms:
        if room_choice == room_num:
            room_history.append(room_num)
            RoomDetails(rooms_details[room_num])
            print('You have Visited the following room(s)',room_history)
            next_room = int(input('Enter your Choice (which room you want to visit next) {} from the given choices : '.format(rooms[room_choice])))
            print('')
            for next_choice in rooms[room_num]:
                if next_room == next_choice:
                    if next_room == 5:
                        room_history.append(next_room)
                        print(rooms[next_room])
                        print('Your Travel History\n',room_history)
                        flag = 1
                    elif next_room == 6:
                        room_history.append(next_room)
                        print(rooms[next_room])
                        print('Your Travel History\n', room_history)
                        flag = 1
                    else:
                        RoomAdventure(next_room, room_history)
                        flag = 1
    if flag == 0:
        print('You can\'t move further in this Direction' )
    return True

# Function to print room details
def RoomDetails(room):
    print('Room Details are\n')
    print('{} is a {}-Colored, {}-Surfaced fruit whose Weight is {}\n'.format(room[0], room[1], room[2], room[3]))
    return True

rooms = {1:[2,4], 2:[1,3,5], 3:[2,5], 4:[5,6], 5:'You Loss', 6:'Congratulations! You Won'}
rooms_details = {1:['Apple', 'Red', 'Soft', '150 grams'], 2:['Orange', 'Yellowish-Orange', 'Rough', '120 grams'],
                 3:['Banana', 'Yellow', 'Soft', '130 grams'], 4:['Pomegranate', 'Red', 'Soft', '140 grams']}

choice = int(input('Do You Want to play the game then enter 1 : '))
print('')
room_history = list()
if choice == 1:
    RoomAdventure(choice, room_history)
else:
    print('Thank You')