from tkinter import *
from tkinter import ttk
import re
from wsgiref import validate


root = Tk()
mainframe = ttk.Frame(root, width=300, height=300)
mainframe.grid()
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)



def check_num(newval, op):
    valid = re.match('\d', newval) is not None
    if op=='key':
        oksofar = re.match('^[0-9]*$', newval) is not None and len(newval) <= 4
        print(newval)
        if oksofar:
            newok = re.match('^[0')
        if not oksofar:
            print('too logn or not num ')
        return oksofar
    elif op=='focusout':
        if not valid:
            print('ansfasf')
    return valid

checknumwrapper = (root.register(check_num), '%P', '%V')

num = StringVar()
ttk.Label(mainframe, text="enter a number").grid(column=0, row=0)
ttk.Entry(mainframe, textvariable=num, validate='all', validatecommand=checknumwrapper).grid(column=0, row=1)


root.mainloop()
