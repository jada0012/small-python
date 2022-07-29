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