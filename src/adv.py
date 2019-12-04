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


# Dictionary of items in each room

items = {
    "arrow": Item("arrow", "This is Green Arrow's arrow.")
    "shield": Item("shield", "This is Captain America's shield.")
    "hammer": Item("hammer", "This is Thor's hammer.")
    "magic sword": Item("magic sword", "This is WonderWoman's sword.")
    "coin": Item("coin", "Coins from Hogwarts.")
}

room["outside"].add_item("shield")
room["foyer"].add_item("arrow")
room["overlook"].add_item("hammer")
room["narrow"].add_item("magic sword")
room["treasure"].add_item("coin")


# Main


# Make a new player object that is currently in the 'outside' room.
new_player = Player("WonderWoman", room["outside"])


# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
# If the user enters "q", quit the game.

while True:
    # Game description
    print("Hi " + new_player.name "! Your current location: " + new_player.room)
    print("Enter a direction: \nNorth: n\nSouth: s\nEast: e\nWest: w\nTo quit: q\n")
    print("To pick up an item, type take <item-name>")
    print("Top drop an item: drop <item-name")

    direction = input("Enter the direction you want to go to: ")
    user_input = direction.strip().lower().split(" ")

    # To quit the game
    if len(user_input) == 1
        if direction not in ["n", "s", "e", "w", "q"]:
            print("Enter a valid direction")
            continue
        if direction == "q":
            print("The Game is Over! Bye")
            break

        # Picking a direction
        current_room = new_player.current_room
        if direction == "n":
            if current_room.n_to is None:
                print("Can't move in that direction.")
                continue
            else:
                new_player.current_room = current_room.n_to

        elif direction == "s":
            if current_room.s_to is None:
                print("Can't move in that direction.")
                continue
            else:
                new_player.current_room = current_room.s_to

        elif direction == "e":
            if current_room.n_to is None:
                print("Can't move in that direction.")
                continue
            else:
                new_player.current_room = current_room.e_to

        elif direction == "w":
            if current_room.n_to is None:
                print("Can't move in that direction.")
                continue
            else:
                new_player.current_room = current_room.w_to

    # Pick up or drop items
    elif len(user_input) == 2:
        if user_input[0] == "take":
            print("Pick up object " + user_input[1])
            if user_input[1] not in new_player.current_room.get_items():
                print("This object cannot be found in this room")
                continue
            else:
                new_player.current_room.delete_item(user_input[1])
                new_player.add_item([user_input[1]])
        elif user_input[0] == "drop":
             print("Drop off object " + user_input[1])
            if user_input[1] not in new_player.get_items():
                print("You don't have " + user_input[1]", you cannot drop it.")
                continue
            else:
                new_player.delete_item([user_input[1]])
                new_player.current_room.add_item(user_input[1])
         else:
             print("Invalid command!")
             continue


    
