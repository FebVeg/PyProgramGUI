import hashlib
import PySimpleGUI as sg

layout = [
    [sg.Frame('SHA256',[
        [sg.Text('File', size=(5, 1)), sg.Input(key="_FILE_"), sg.FileBrowse(button_text="Open", size=(5, 1))],
        [sg.Button('Calculate')]
    ])]
]

window = sg.Window('SHA256 Calculator - FebVeg', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    
    elif event == 'Calculate':
        filename = values['_FILE_']
        sha256_hash = hashlib.sha256()
        # Apro il file in modalità RB
        with open(filename, "rb") as _file:
            # Leggo i blocchi
            for blocco_byte in iter(lambda: _file.read(4096), b""):
                sha256_hash.update(blocco_byte)
            # Printo il risultato
            sg.Print(sha256_hash.hexdigest())

window.close()
