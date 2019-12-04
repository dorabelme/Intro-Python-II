# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item


class Room:
    def __init__(self, name, description, n_to, s_to, w_to, e_to):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.w_to = w_to
        self.e_to = e_to
        self.items = []

    def __str__(self):
        return f"Name: {self.name} \Description: {self.description} \nN_to: {self.n_to}\nS_to: {self.s_to}\nE_to: {self.e_to}\nW_to: {self.w_to}\nItems in the room : " + {str(self.items)}"

    def get_items(self):
        return self.items

    def add_item(self, item):
        return self.items.append(item)

    def delete_item(self, item):
        return self.items.remove(item)
