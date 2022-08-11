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