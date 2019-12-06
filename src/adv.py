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
earlier adventurers.The only exit is to the south. """),

    'cyber': Room("Cyber Room", """You've found the long-lost cybertruck. You're a lucky person, it's all yours now.""")
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
room['narrow'].s_to = room['cyber']
room['cyber'].n_to = room['narrow']


# Dictionary of items in each room

items = {
    "arrow": Item("arrow", "This is Green Arrow's arrow."),
    "shield": Item("shield", "This is Captain America's shield."),
    "hammer": Item("hammer", "This is Thor's hammer."),
    "sword": Item("sword", "This is WonderWoman's sword."),
    "coin": Item("coin", "Coins from Hogwarts."),
    "truck": Item("truck", "It's a Tesla CyberTruck.")
}

room["outside"].add_item(items["shield"])
room["foyer"].add_item(items["arrow"])
room["overlook"].add_item(items["hammer"])
room["narrow"].add_item(items["sword"])
room["treasure"].add_item(items["coin"])
room["cyber"].add_item(items["truck"])


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
    # Winning condition
    if len(new_player.get_inventory()) == 6:
        print(f"You've won the game {new_player.name}!")
        break

    # Game description
    print("\n")
    print("Hi " + new_player.name +
          "! Your current location: " + new_player.current_room.name + "\n")
    print(
        f"Items in the room: {[item.name for item in new_player.current_room.get_items()]}")
    print(
        f"Your current inventory is: {[item.name for item in new_player.get_inventory()]}")
    print(f"Your current score is: {new_player.score}\n")
    print("Enter a direction: \nNorth: n\nSouth: s\nEast: e\nWest: w\nTo quit: q\n")
    print("To pick up an item, type take/get <item-name>")
    print("Top drop an item: drop <item-name\n")

    direction = input("Enter the direction you want to go to: ")
    user_input = direction.strip().lower().split(" ")

    room_items = {
        item.name: item for item in new_player.current_room.get_items()}

    # To quit the game
    if len(user_input) == 1:
        if direction not in ["n", "s", "e", "w", "q", "i", "inventory"]:
            print("Enter a valid direction\n")
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
            if current_room.e_to is None:
                print("Can't move in that direction.")
                continue
            else:
                new_player.current_room = current_room.e_to

        elif direction == "w":
            if current_room.w_to is None:
                print("Can't move in that direction.")
                continue
            else:
                new_player.current_room = current_room.w_to
        elif direction == 'i' or direction == 'inventory':
            print(f"\nYour inventory: {new_player.get_inventory()}")

    # Pick up or drop items
    elif len(user_input) == 2:
        verb = user_input[0]
        item_str = user_input[1]

        if verb == "take" or verb == 'get':
            if item_str not in room_items:
                print("This object cannot be found in this room")
                continue
            else:
                item = room_items[item_str]

                new_player.current_room.delete_item(item)
                new_player.add_item(item)
                item.on_take()

        elif verb == "drop":
            if item_str not in room_items:
                print("You don't have " + item_str + ", you cannot drop it.")
                continue
            else:
                item = room_items[item_str]

                new_player.delete_item(item)
                new_player.current_room.add_item(item)
                item.on_drop()
        else:
            print("Invalid command!")
            continue
