import PySimpleGUI as sg
import os
import webbrowser
from pathlib import Path


sg.popup('Study mode initiated', auto_close=True, )

os.system("taskkill /f /im  discord.exe")

brave = Path("C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe")

open(brave)

webbrowser.open_new('https://cc-jam.moodle.renweb.com/')

