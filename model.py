import pickle

"""
File with MODEL part of MVC pattern.
"""


def check(filename):
    """
    try to open file with database, if it doesn't exist - create new file

    >>> check('lab1.pickle')

    >>> check('test.pickle')

    >>> import os
    >>> if os.path.exists('test.pickle'): os.remove('test.pickle')
    """
    try:
        open(filename, 'rb').close()
    except IOError:
        open(filename, 'wb').close()


def show(filename):
    """
    show all item from database, if db is empty - return empty string

    >>> import os
    >>> if os.path.exists('test.pickle'): os.remove('test.pickle')
    >>> check('test.pickle')
    >>> show('test.pickle')
    ''
    >>> write(['dish', 6], 'test.pickle')
    >>> show('test.pickle')
    [{'name': 'dish', 'val': 6}]
    >>> if os.path.exists('test.pickle'): os.remove('test.pickle')
    """
    try:
        return pickle.load(open(filename, "rb"))
    except EOFError:
        return ''


def calc(list, filename):
    """
    calculates calories and return number of it

    >>> calc([{'name':'0123456789', 'val':0}], 'lab1.pickle')
    '0123456789'
    >>> calc([{'name':pickle.load(open('lab1.pickle', "rb"))[0]['name'],
    ... 'val':0}], 'lab1.pickle')
    0
    """
    res = 0
    file = pickle.load(open(filename, "rb"))
    for element in list:
        b = [d for d in file if d['name'] == element['name']]
        if not b:
            return element['name']
        res += int(b[0]['val'])*int(element['val'])
    return res


def write(val, filename):
    """
    try to write new item into database

    >>> write(['dish', 6], 'lab1.pickle')

    """
    try:
        b = pickle.load(open(filename, "rb"))
        if [d for d in b if d['name'] == val[0]]:
            b.remove([d for d in b if d['name'] == val[0]][0])
        b.append({'name': val[0], 'val': val[1]})
    except EOFError:
        b = [{'name': val[0], 'val': val[1]}]
    pickle.dump(b, open(filename, "wb"))
