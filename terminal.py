import PySimpleGUI as sg
from os import popen

layout = [
    [sg.Frame('Console',[
        [sg.Output(size=(80, 25), key="output")]
    ])],


    [sg.Frame('Command Prompt',[
        [sg.Text('Command:', size=(None, 1)), sg.Input(key='cmd'), sg.Button('Execute'), sg.Button('Clear')]
    ])],
]

window = sg.Window('Command Prompt v.1.0', layout)

while True:
    try:
        event, values = window.read()

        if event == sg.WIN_CLOSED:           # always,  always give a way out!    
            break
        
        elif event == "Execute":
            check = popen(str(values['cmd'])).read()
            print("Command Executed: " + values['cmd'])
            print(check)

        elif event == "Clear":
            window.find_element('output').Update('')

    except Exception as identifier:
        print(identifier)
window.close()
