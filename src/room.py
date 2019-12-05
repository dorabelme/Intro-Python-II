# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item


class Room:
    def __init__(self, name, description, n_to=None, s_to=None, w_to=None, e_to=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.w_to = w_to
        self.e_to = e_to
        self.items = []

    def __str__(self):
        # return f"Name: {self.name}"

        _str = f"Name: {self.name} \nDescription: {self.description} \n"
        _str += f"Items in the room : {self.items}"

        return _str

        # if self.n_to:
        #     _str +=

        # return f"Name: {self.name} \nDescription: {self.description} \nN_to: {self.n_to.name}\nS_to: {self.s_to.name}\nE_to: {self.e_to.name}\nW_to: {self.w_to.name}\nItems in the room : {self.items}"

    def get_items(self):
        return self.items

    def add_item(self, item):
        return self.items.append(item)

    def delete_item(self, item):
        return self.items.remove(item)
