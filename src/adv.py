from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
items = {
    'broom': Item('broom', 'A broom for clearing debris'),
    'key': Item('key', 'a key for opening doors'),
    'sword': Item('sword', 'a sword for slicing people'),
    'bag': Item('bag', 'a bag for holding items easier'),
    'hat': Item('hat', 'a indiana jones style hat'),
    'light': Item('light', 'a light for seeing things')
}

room['outside'].addItem(items['broom'])
room['outside'].addItem(items['key'])
room['foyer'].addItem(items['sword'])
room['overlook'].addItem(items['hat'])
room['narrow'].addItem(items['light'])
room['treasure'].addItem(items['bag'])


#
# Main
#

# Make a new player object that is currently in the 'outside' room.


print('Welcome to our adventure game!')
playerName = input('Please enter your name: ')
p = Player(playerName, room['outside'])

# figuring out how i want to access and change rooms
# print(p.room.n_to)

#p.room = p.room.n_to
# print(p)
# print(f'whats north now? {p.room.n_to}')F

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

'''print(p.__dict__)
print(p.room.__dict__)
print(p.room.n_to.__dict__) '''  # testing what gets returned with the __dict__


def validMove(movement):
    currentRoom = p.room
    if currentRoom.__dict__[f'{movement}_to'] == None:
        print("There is nothing that direction!")
    else:
        p.room = currentRoom.__dict__[f'{movement}_to']


while True:
    currentRoom = p.room
    movementChoice = ['n', 'e', 's', 'w']
    items = p.room.items

    print(f"Here's you're info: \n {p}")
    print(f'\nItems in this area:  ')
    for i in items:
        print(i)

    print('\n')
    userChoice = input(
        'What do you want to do? You can Move n, e, s, or w...or you can "pickup" or "drop" items --drop sword-- You can also enter q to quit: ')

    if userChoice in movementChoice:
        validMove(userChoice)

    elif userChoice == "q":
        print("Thanks for playing!")
        exit()
    else:
        print("\nThat is not allowed movement input.")
