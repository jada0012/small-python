import PySimpleGUI as sg 
import random

sg.theme('Dark Blue 8')
MaxRow = MaxCol = 10
board = [[randint(0,1) for j in range(MaxCol)] for i in range(MaxRow)]
layout=[[sg.Button('?', size=(4,2), key=(i,j), pad=(0,0)) for j in range(MaxCol)] for i in range(MaxRow)]

window= sg.Window('Minesweeper', layout)
while True:
    event, values = window.read()
    if i
