# Write a class to hold player information, e.g. what room they are in
# currently.

from item import Item


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __str__(self):
        return f"Name: {self.name} \Room: {self.current_room} \n Your  Inventory: " + str(self.inventory)"

    def get_inventory(self):
        return self.inventory

    def add_item(self):
        return self.inventory.append(item)

    def delete_item(self):
        return self.inventory.remove(item)
