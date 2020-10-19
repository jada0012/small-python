import PySimpleGUI as sg 


sg.theme=('BluePurple')
layout = [[sg.Text('My Persistent Window'), sg.Text(size=(15,1), key='-OUTPUT-')],
                    [sg.Input(key='-IN-')],
                    [sg.Button('Read'), sg.Exit()]]

window=sg.Window('Title', layout)
while True:
    event, values = window.read()
    print(event, values)
    if event==sg.WIN_CLOSED or event=='Exit':
        break


window.close()



