from cgitb import text
import ctypes, sys
from tkinter import *
from tkinter import ttk
import time
import re

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
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

    def validateTime(newval):
        errmsg = ''
        valid = re.match('\d{1,2}:\d{2}', newval) is not None
        


    root = Tk()
    root.title("block sites")
    mynotebook = ttk.Notebook(root)
    mynotebook.grid()


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
    timeElapsed = StringVar()
    label = ttk.Label(mainframe, text="time blocked: ", textvariable=timeElapsed)
    label['textvariable'] = timeElapsed


    frametwo = Frame(root,width=300, height=300, bg="blue")
    frametwo.columnconfigure(0, weight=1)
    frametwo.columnconfigure(1, weight=1)
    frametwo.columnconfigure(2, weight=1)
    frametwo.rowconfigure(0, weight=1)
    frametwo.rowconfigure(1, weight=1)

    start_time_hours = IntVar()
    # start_time_mins = IntVar()
    end_time_hours = IntVar()
    # end_time_mins = IntVar()

    ttk.Label(frametwo, text="enter start time").grid(column=0, row=0)
    ttk.Label(frametwo, text="enter end time").grid(column=0, row=1)

    ttk.Entry(frametwo, textvariable=start_time_hours).grid(column=1, row=0)
    # ttk.Entry(frametwo, textvariable=start_time_mins).grid(column=2, row=0)
    ttk.Entry(frametwo, textvariable=end_time_hours).grid(column=1, row=1)
    # ttk.Entry(frametwo, textvariable=end_time_mins).grid(column=2, row=1)
    mynotebook.add(mainframe, text="based")
    mynotebook.add(frametwo, text="notbased")
    root.mainloop()
    

    
    
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)