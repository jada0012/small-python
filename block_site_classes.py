import ctypes, sys
from multiprocessing.sharedctypes import Value
from datetime import datetime, date
from tkinter import *
from tkinter import ttk
import traceback
import time
import re
import logging

LOG_FILENAME = 'logging_example.out'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)



blocklist = ['twitter.com', 'tumblr.com', 'discord.com', 'instagram.com', 'reddit.com']
REDIRECT = '127.0.0.1'
HOST_PATH = r'C:\Windows\System32\drivers\etc\hosts'


class BlockSiteApp(Tk):
    def __init__(self):
        super().__init__()

        self.title("Block Sites")
        self.notebook = ttk.Notebook(self)

        self.Frame1 = BasicBlock(self.notebook)
        self.Frame2 = ScheduleBlock(self.notebook)
        self.notebook.add(self.Frame1, text='no frills block')
        self.notebook.add(self.Frame2, text='daily time block ')

        self.notebook.grid(column=0, row=0)


class BasicBlock(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        ttk.Button(self, text="Block", command=self.block).grid(column=0, row=0, columnspan=2)
        ttk.Button(self, text="Unblock" ,command=self.unblock).grid(column=3, row=0, columnspan=2)

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
    


class ScheduleBlock(ttk.Frame):
    def __init__(self, container):
        super().__init__()
                
        start_time_hours = StringVar()
        end_time_hours = StringVar()
        testVar = StringVar()
        errMsg = StringVar()
        # validate_time_wrapper = (app.register(self.validateTime), '%P', '%V')


        ttk.Label(self, text="enter start time").grid(column=0, row=0, sticky=W)
        ttk.Label(self, text="enter end time").grid(column=0, row=1, sticky=W)
        ttk.Label(self, textvariable=testVar).grid(column=0, row=3)
        ttk.Label(self, textvariable=errMsg).grid(column=0, row=4)

        ttk.Entry(self, textvariable=start_time_hours, validate='key').grid(column=1, row=0)
        ttk.Entry(self, textvariable=end_time_hours, validate='key', ).grid(column=1, row=1)
        btn = ttk.Button(self, text='submit')
            

    def validateTime(self, newval, op):
        valid = re.match('^[0-9]{1,2}:?[0-9]{2}$', newval) is not None
        if op == 'key':
            oknow = re.match('^[0-9]*:?[0-9]*$', newval) is not None and len(newval) <= 5
        
            if not oknow:
                print(newval)
                print('error')
            return oknow
        return valid
    


def is_admin(): 
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    try:
        app = BlockSiteApp()
       
        app.mainloop()
    except :
       logging.exception('got error')
       raise
      
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    