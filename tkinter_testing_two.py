# from tkinter import *
# from tkinter import ttk
# import re
# from wsgiref import validate


# root = Tk()
# mainframe = ttk.Frame(root, width=300, height=300)
# mainframe.grid()
# root.rowconfigure(0, weight=1)
# root.rowconfigure(1, weight=1)



# def check_num(newval, op):
#     valid = re.match('\d', newval) is not None
#     if op=='key':
#         oksofar = re.match('^[0-9]*$', newval) is not None and len(newval) <= 4
#         print(newval)
#         if oksofar:
#             newok = re.match('^[0')
#         if not oksofar:
#             print('too logn or not num ')
#         return oksofar
#     elif op=='focusout':
#         if not valid:
#             print('ansfasf')
#     return valid

# checknumwrapper = (root.register(check_num), '%P', '%V')

# num = StringVar()
# ttk.Label(mainframe, text="enter a number").grid(column=0, row=0)
# ttk.Entry(mainframe, textvariable=num, validate='all', validatecommand=checknumwrapper).grid(column=0, row=1)


# # root.mainloop()
# # Create an instance of tkinter frame
# win=Tk()

# # Set the size of the Tkinter window
# win.geometry("700x350")

# # Define a function to print something inside infinite loop
# condition=True
# def infinite_loop():
#    if condition:
#         Label(win, text="Infinite Loop!", font="Arial, 25").pack()

#    # Call the infinite_loop() again after 1 sec 
#         win.after(1000, infinite_loop)

# def start():
#    global condition
#    condition=True

# def stop():
#    global condition
#    condition=False


# # Create a button to start the infinite loop
# start = Button(win, text= "Start the Loop", font="Arial, 12", command=start).pack()
# stop = Button(win, text="Stop the Loop", font="Arial, 12", command=stop).pack()

# # Call the infinite_loop function after 1 sec.
# win.after(1000, infinite_loop)

# win.mainloop()
import tkinter as tk
import time

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="")
        self.label.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)

app=App()