import sys


class Map:

    def __int__(self):
        self.list = []

    def insert(self, addKey, value):
        not_in_list = True
        for i, (key, _) in enumerate(self.list):

            # If there is a key update it
            if addKey == key:
                not_in_list = False
                self.list[i] = (addKey, value)
                break
        if not_in_list:
            self.list.append((key, value))

    def search(self, searchKey):
        for key, value in self.list:
            if searchKey == key:
                return value
        return None


