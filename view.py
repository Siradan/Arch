"""
File wuth VIEW part of MVC pattern.
Displays messages in the terminal for user assistance.
"""


def get():
    """
    read code from input and return code index
    """
    input = raw_input('Command: ').strip()
    list = ['show', 'calc', 'write', 'help', 'exit']
    if input in list:
        return list.index(input)
    else:
        return 5


def table(list):
    """
    Display the list of products from LIST variable.
    """
    print ('Calories table:')
    for index, element in enumerate(list, 1):
        buffer_0 = str(index).ljust(3)
        buffer_0 += element.get('name').ljust(25)
        buffer_0 += str(element.get('val'))

        print buffer_0


def input():
    """
    Read and return entered list of products and number of them.
    """
    return raw_input('Enter calculation (example: "potato 3 tomato 5"): ')


def output(val):
    """
    Outputs the result of counting.
    """
    print 'Calories result:', val


def new():
    """
    Read and return new entered product and number calories in it.
    """
    return raw_input('Enter new item (example: "potato 3"): ')


def help():
    """
    Print tutorial.
    """
    print '"show": Show table of items with names and calories per gram'
    print '"calc": Calculate calories'
    print '"write": Add new item to table'
    print '"exit": Close program'


def error():
    """
    Print error message .
    """
    print 'Unidentified command'


def notfound(list):
    """
    Prints item that cannot be found in input list on products.
    """
    print 'Unidentified:', list


def bye():
    """
    Print "Bye" message.
    """
    print 'Bye'
