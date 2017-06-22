from serializers.serializers import Serialize


class Model:
    """
    Model part of MVC
    """

    def __init__(self, serializer):
        """
        Constructor for Model class
        """
        self._serializer = Serialize(serializer)
        self.sorted = Sorted()
        self.database = None

    def __iter__(self):
        """
        Return iterator for database
        """
        return Iterator(self.database, self.sorted.get_order())

    def load(self, filename):
        """
        Load database from file
        """
        self.database = self._serializer.load(filename)
        self.sorted = Sorted(self.database)

    def save(self, filename):
        """
        Save database to file
        """
        self._serializer.save(filename, self.database)

    def sort(self, flag):
        if flag == 0:
            self.sorted.sort_by_val_top(self.database)
        elif flag == 1:
            self.sorted.sort_by_val_bottom(self.database)
        elif flag == 2:
            self.sorted.sort_by_name_top(self.database)
        elif flag == 3:
            self.sorted.sort_by_name_bottom(self.database)

    def return_db(self):
        """
        Return database
        """
        return self.database

    def count(self, list):
        """
        Calculates calories and return number of it
        """
        res = 0
        for element in list:
            b = [d for d in self.database if d['name'] == element['name']]
            if not b:
                return element['name']
            res += int(b[0]['val']) * int(element['val'])
        return res

    def add_item(self, val):
        """
        try to write new item into database
        """
        if [d for d in self.database if d['name'] == val[0]]:
            self.database.remove([d for d in self.database if
                                  d['name'] == val[0]][0])

        self.database.append({'name': val[0], 'val': val[1]})
        self.sorted = Sorted(self.database)


class Iterator:
    """
    Iterator for database
    """
    def __init__(self, list, order):
        self.list = list
        self.order = order
        self.current = self.list[self.order[0]]
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.order):
            res = self.current
            if self.i + 1 < len(self.order):
                self.current = self.list[self.order[self.i + 1]]
            self.i += 1
            return res
        else:
            raise StopIteration()


class Format:
    """
    Class for transform strings to lists
    """
    def line_to_list(self, s):
        """
        Format input string from console to list
        """
        arg0 = 'name'
        arg1 = 'val'
        return [{arg0: s[i * 2], arg1: s[i * 2 + 1]}
                for i in range((int(len(s) / 2)))]


class Sorted:
    """
    Sorting list
    """
    def __init__(self, list=None):
        if list is None:
            list = []
        self.order = []
        for i in enumerate(list):
            self.order.append(i[0])

    def get_order(self):
        """
        Return order of sorted elements
        """
        return self.order

    def sort_by_val_top(self, list):
        """
        Ascending sort list's elements by val ascending
        """
        self.order = []
        for i, elem in enumerate(list):
            j = 0
            while j < len(self.order):
                if int(elem['val']) > int(list[self.order[j]]['val']):
                    self.order.insert(j, i)
                    break

                j += 1
            if j == len(self.order):
                self.order.append(i)

    def sort_by_val_bottom(self, list):
        """
        Decreasing sort list's elements by val ascending
        """
        self.order = []
        for i, elem in enumerate(list):
            j = 0
            while j < len(self.order):
                if int(elem['val']) < int(list[self.order[j]]['val']):
                    self.order.insert(j, i)
                    break

                j += 1
            if j == len(self.order):
                self.order.append(i)

    def sort_by_name_top(self, list):
        """
        Ascending sort list's elements by name ascending
        """
        self.order = []
        for i, elem in enumerate(list):
            j = 0
            while j < len(self.order):
                if elem['name'] < list[self.order[j]]['name']:
                    self.order.insert(j, i)
                    break

                j += 1
            if j == len(self.order):
                self.order.append(i)

    def sort_by_name_bottom(self, list):
        """
        Decreasing sort list's elements by name ascending
        """
        self.order = []
        for i, elem in enumerate(list):
            j = 0
            while j < len(self.order):
                if elem['name'] > list[self.order[j]]['name']:
                    self.order.insert(j, i)
                    break

                j += 1
            if j == len(self.order):
                self.order.append(i)
