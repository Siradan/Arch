import view
from model import show, calc, write, check
from view import get, table, output, new, error, input, bye, notfound, help

"""
Main file for app.
CONTROLLER part of MVC pattern.
Checks the presence of a file,
displays a hint,
and controls the application logic.
"""

dbfile = 'lab1.pickle'
check(dbfile)
help()
code = get()
arg0 = 'name'
arg1 = 'val'
while code != 4:
    if code == 0:
        table(show(dbfile))
    elif code == 1:
        s = input().split()
        print(s)
        print((len(s))/2)
        res = calc(
            [{arg0: s[i*2], arg1: s[i*2+1]} for i in range((len(s))/2)],
            dbfile)
        if isinstance(res, basestring):
            notfound(res)
        else:
            output(res)
    elif code == 2:
        arg = new().split()
        if len(arg) != 2:
            error()
        else:
            try:
                if int(arg[1]) > 0:
                    write(arg, dbfile)
                else:
                    error()
            except ValueError:
                error()
    elif code == 3:
        view.help()
    else:
        error()

    code = get()
bye()
