from tkinter import *
from tkinter import ttk

# root = Tk()

# content = ttk.Frame(root, padding=(3,3,12,12))
# frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100)
# namelbl = ttk.Label(content, text="Name")
# name = ttk.Entry(content)

# onevar = BooleanVar()
# twovar = BooleanVar()
# threevar = BooleanVar()

# onevar.set(True)
# twovar.set(False)
# threevar.set(True)

# one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
# two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
# three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
# ok = ttk.Button(content, text="Okay")
# cancel = ttk.Button(content, text="Cancel")

# content.grid(column=0, row=0, sticky=(N, S, E, W))
# frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
# namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
# name.grid(column=3, row=1, columnspan=2, sticky=(N,E,W), pady=5, padx=5)
# one.grid(column=0, row=3)
# two.grid(column=1, row=3)
# three.grid(column=2, row=3)
# ok.grid(column=3, row=3)
# cancel.grid(column=4, row=3)

# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
# content.columnconfigure(0, weight=3)
# content.columnconfigure(1, weight=3)
# content.columnconfigure(2, weight=3)
# content.columnconfigure(3, weight=1)
# content.columnconfigure(4, weight=1)
# content.rowconfigure(1, weight=1)

# root.mainloop()
# import ctypes, sys


# def is_admin():
#     try:
#         return ctypes.windll.shell32.IsUserAnAdmin()
#     except:
#         return False
# if is_admin():
#     def unblock():
#         blocklist = ['twitter.com', 'tumblr.com', 'discord.com']
#         redirect = '127.0.0.1'
#         host_path = r'C:\Windows\System32\drivers\etc\hosts'
#         count = 1

#         with open(host_path, 'r+') as hostfile:
#             lines = hostfile.readlines()
#             hostfile.seek(0)
#             for line in lines:
#                 if not  any(site in line for site in blocklist):
#                     print(f'{line}')
#                     hostfile.write(line)
#                 hostfile.truncate()
                    


#     unblock()
#     input()
# else:
#     ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

# root = Tk()
# root.geometry("500x500")
# mynotebook = ttk.Notebook(root)
# mynotebook.grid()
# f1 = Frame(mynotebook, width=500, height=500, bg="blue")
# f2 = Frame(mynotebook, width=500, height=500, bg="green")

# f1.grid(column=0, row=0)
# f2.grid(column=0, row=0)

# mynotebook.add(f1, text="one")
# mynotebook.add(f2, text="two")


# root.mainloop()
import re
# x = re.match('\d{1,2}:\d{2}', "cicj")
root = Tk()
errmsg = StringVar()
formatmsg = "Zip should be ##### or #####-####"

def check_zip(newval, op):
    errmsg.set('')
    valid = re.match('^[0-9]{5}(\-[0-9]{4})?$', newval) is not None
    btn.state(['!disabled'] if valid else ['disabled'])
    if op=='key':
        ok_so_far = re.match('^[0-9\-]*$', newval) is not None and len(newval) <= 10
        print(newval)
        if not ok_so_far:
            errmsg.set(formatmsg)
        return ok_so_far
    elif op=='focusout':
        if not valid:
            errmsg.set(formatmsg)
    return valid
check_zip_wrapper = (root.register(check_zip), '%P', '%V')

zip = StringVar()
f = ttk.Frame(root)
f.grid(column=0, row=0)

ttk.Label(f, text='Name:').grid(column=0, row=0, padx=5, pady=5)
ttk.Entry(f).grid(column=1, row=0, padx=5, pady=5)
ttk.Label(f, text='Zip:').grid(column=0, row=1, padx=5, pady=5)
e = ttk.Entry(f, textvariable=zip, validate='all', validatecommand=check_zip_wrapper)
e.grid(column=1, row=1, padx=5, pady=5)
btn = ttk.Button(f, text="Process")
btn.grid(column=2, row=1, padx=5, pady=5)
btn.state(['disabled'])
msg = ttk.Label(f, font='TkSmallCaptionFont', foreground='red', textvariable=errmsg)
msg.grid(column=1, row=2, padx=5, pady=5, sticky='w')

root.mainloop()

import ctypes, sys
from multiprocessing.sharedctypes import Value
from datetime import datetime, date
from tkinter import *
from tkinter import ttk
import time
import re
blocklist = ['twitter.com', 'tumblr.com', 'discord.com', 'instagram.com', 'reddit.com']
redirect = '127.0.0.1'
host_path = r'C:\Windows\System32\drivers\etc\hosts'


def block():
    
    with open(host_path, 'r+') as hostfile:
        
        hosts = hostfile.read()
        for site in blocklist:
            if site not in hosts:
                hostfile.write(redirect + " " + site + "\n")
                hostfile.write(redirect + " " + "www." + site + "\n")
    

def unblock():
    with open(host_path, 'r+') as hostfile:
        lines = hostfile.readlines()
        hostfile.seek(0)
        for line in lines:
            if not  any(site in line for site in blocklist):
                hostfile.write(line)
            hostfile.truncate()




root = Tk()
root.title("block sites")
mynotebook = ttk.Notebook(root)
mynotebook.grid()

def validateTime(newval, op):
    valid = re.match('^[0-9]{1,2}:?[0-9]{2}$', newval) is not None
    btn.state(['!disabled'] if valid else ['disabled'])
    if op == 'key':
        oknow = re.match('^[0-9]*:?[0-9]*$', newval) is not None and len(newval) <= 5
    
        if not oknow:
            print(newval)
            print('error')
        return oknow
    return valid

            
validate_time_wrapper = (root.register(validateTime), '%P', '%V')

mainframe = ttk.Frame(root, width=300, height=300, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)



ttk.Button(mainframe, text="Block", command=block).grid(column=0, row=0, columnspan=2)
ttk.Button(mainframe, text="Unblock" ,command=unblock).grid(column=3, row=0, columnspan=2)

def testStuff(*args):
    try:
        starthours, startmins = start_time_hours.get().split(':')
        endhours, endmins = end_time_hours.get().split(':')

        if (int(startmins) > 59) or (int(endmins)> 59):
            errMsg.set('enter correct times doofus')

        
        current_year = date.today().year
        current_month = date.today().month
        current_day = date.today().day

        if int(endhours) < int(starthours):
            end_day = current_day + 1
        else:
            end_day = current_day

        starttime = datetime(current_year, current_month, current_day, int(starthours), int(startmins))
        endtime = datetime(current_year, current_month, end_day, int(endhours), int(endmins))



        if (datetime.now() > starttime) and (datetime.now() < endtime):
            status = 'you are in the blocking hours'
            block()
        else:
            status = 'you are not in the blocking hours'
            unblock()


        print(f'{datetime.now()=} {current_day=}, {end_day=}')
        testVar.set(status)
    except ValueError:
        pass


frametwo = Frame(root,width=300, height=300)
frametwo.columnconfigure(0, weight=1)
frametwo.columnconfigure(1, weight=1)
frametwo.columnconfigure(2, weight=1)
frametwo.rowconfigure(0, weight=1)
frametwo.rowconfigure(1, weight=1)
frametwo.rowconfigure(2, weight=1)
frametwo.rowconfigure(3, weight=1)
frametwo.rowconfigure(4, weight=1)

start_time_hours = StringVar()
end_time_hours = StringVar()
testVar = StringVar()
errMsg = StringVar()

ttk.Label(frametwo, text="enter start time").grid(column=0, row=0, sticky=W)
ttk.Label(frametwo, text="enter end time").grid(column=0, row=1, sticky=W)
ttk.Label(frametwo, textvariable=testVar).grid(column=0, row=3)
ttk.Label(frametwo, textvariable=errMsg).grid(column=0, row=4)

ttk.Entry(frametwo, textvariable=start_time_hours, validate='key', validatecommand=validate_time_wrapper).grid(column=1, row=0)
ttk.Entry(frametwo, textvariable=end_time_hours, validate='key', validatecommand=validate_time_wrapper).grid(column=1, row=1)
btn = ttk.Button(frametwo, text='submit', command=testStuff)


btn.grid(column=1, row=2)
btn.state(['disabled'])
mynotebook.add(mainframe, text="indefinite block")
mynotebook.add(frametwo, text="time-based block")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    
    root.mainloop()
    

    
    
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)







blocklist = ['twitter.com', 'tumblr.com', 'discord.com', 'instagram.com', 'reddit.com']
REDIRECT = '127.0.0.1'
HOST_PATH = r'C:\Windows\System32\drivers\etc\hosts'


class Basic:

    def __init__(self, master):
        frame_one = ttk.Frame(master)
        frame_one.grid(column=0, row=0, sticky=(N, W, E, S))
        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=1)
        master.columnconfigure(2, weight=1)
        master.columnconfigure(3, weight=1)
        master.rowconfigure(0, weight=1)
        master.rowconfigure(1, weight=1)

        ttk.Button(frame_one, text="Block", command=self.block).grid(column=0, row=0, columnspan=2)
        ttk.Button(frame_one, text="Unblock" ,command=self.unblock).grid(column=3, row=0, columnspan=2)


    def block(self):
        with open(HOST_PATH, 'r+') as hostfile:
            hosts = hostfile.read()
            for site in blocklist:
                if site not in hosts:
                    hostfile.write(REDIRECT + " " + site + "\n")
                    hostfile.write(REDIRECT + " " + "www." + site + "\n")

    def unblock(self):
        with open(HOST_PATH, 'r+') as hostfile:
            lines = hostfile.readlines()
            hostfile.seek(0)
            for line in lines:
                if not  any(site in line for site in blocklist):
                    hostfile.write(line)
                hostfile.truncate()

root = Tk()
Basic(root)

import tkinter as tk
from tkinter import ttk

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Example")
        self.geometry('300x300')

        self.notebook = ttk.Notebook(self)

        self.Frame1 = Frame1(self.notebook)
        self.Frame2 = Frame2(self.notebook)

        self.notebook.add(self.Frame1, text='Frame1')
        self.notebook.add(self.Frame2, text='Frame2')

        self.notebook.pack()

class Frame1(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        self.labelA = ttk.Label(self, text = "This is on Frame One")
        self.labelA.grid(column=1, row=1)

class Frame2(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        self.labelB = ttk.Label(self, text = "This is on Frame Two")
        self.labelB.grid(column=1, row=1)

if __name__ == '__main__':
    app = MainApplication()
    app.mainloop()