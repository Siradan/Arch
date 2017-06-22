class View:
    """
    File with VIEW part of MVC pattern.
    Displays messages in the terminal for user assistance.
    """

    def get_command(self):
        """
        read code from input and return code index
        """
        get = input('Command: ').strip()
        list = ['show',
                'calc',
                'write',
                'help',
                'exit',
                'sort 0',
                'sort 1',
                'sort 2',
                'sort 3']
        if get in list:
            return list.index(get)
        else:
            return 5

    def show_db(self, iterator):
        """
        Display the list of products from LIST variable.
        """
        print ('Calories table:')
        for index, element in enumerate(iterator, 1):
            print(str(index).ljust(3),
                  element.get('name').ljust(25),
                  str(element.get('val')))

    def input(self):
        """
        Read and return entered list of products and number of them.
        """
        return input('Enter calculation (example: "potato 3 tomato 5"): ')

    def output(self, val):
        """
        Outputs the result of counting.
        """
        print('Calories result:', val)

    def new(self):
        """
        Read and return new entered product and number calories in it.
        """
        return input('Enter new item (example: "potato 3"): ')

    def show_menu(self):
        """
        Print tutorial.
        """
        print('"help": Print tutorial')
        print('"show": Show table of items with names and calories per gram')
        print('"calc": Calculate calories')
        print('"write": Add new item to table')
        print('"sort 0": Ascending sort of items by value')
        print('"sort 1": Decreasing sort of items by value')
        print('"sort 2": Ascending sort of items by name')
        print('"sort 3": Decreasing sort of items by name')
        print('"exit": Close program')

    def error(self):
        """
        Print error message .
        """
        print('Unidentified command')

    def notfound(self, list):
        """
        Prints item that cannot be found in input list on products.
        """
        print('Unidentified:', list)
