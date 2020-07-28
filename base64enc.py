import PySimpleGUI as sg
from os import path 
import base64

tab1_layout =  [
    [sg.Frame('Enter code or text',[
        [sg.Multiline(key='testo')]
    ])],
    [sg.Button('Encode Text')]   
]    

tab2_layout = [
    [sg.Frame('Enter a file',[
        [sg.Input(key='doc'), sg.FileBrowse(button_text="Open", size=(4, 1))]
    ])],
    [sg.Button('Encode File')]
]    

layout = [[sg.TabGroup([[sg.Tab('Text', tab1_layout), sg.Tab('File', tab2_layout)]])]]   

window = sg.Window('Base64 Encoder - FebVeg', layout, default_element_size=(40, 10))    

while True:    
    event, values = window.read()    

    if event == sg.WIN_CLOSED:           # always,  always give a way out!    
        break  

    elif event == "Encode Text":
        text = values['testo']
        if len(text) > 1:
            try:
                text_bytes = text.encode('ascii')
                base64_bytes = base64.b64encode(text_bytes)
                base64_message = base64_bytes.decode('ascii')
                sg.Print("Encoded strings\n")
                sg.Print(base64_message)
            except Exception as text_enc_err:
                sg.Print(text_enc_err)

    elif event == "Encode File":
        document = values['doc']
        if len(document) > 1:
            if path.exists(document):
                try:
                    sg.Print(document)
                    with open(document, 'rb') as binary_file:
                        binary_file_data = binary_file.read()
                        base64_encoded_data = base64.b64encode(binary_file_data)
                        base64_message = base64_encoded_data.decode('utf-8')
                        sg.Print("Encoded File\n")
                        sg.Print(base64_message)
                except Exception as doc_enc_err:
                    sg.Print(doc_enc_err)
            
