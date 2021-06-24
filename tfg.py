import PySimpleGUI as sg 
import os

the_path = sg.popup_get_folder("Pick a folder, any folder")
files = os.listdir(the_path)
sg.popup_scrolled('\n'.join(files))
