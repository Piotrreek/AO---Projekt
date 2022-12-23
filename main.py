import os
import PySimpleGUI as sg
file_types = [("PNG (*.png)", "*.png"),
              ("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]

def main():
    layout = [
        [sg.Image(key="-IMAGE-")],
        [
            sg.Text("Image File"),
            sg.Input(size=(25, 1), key="-FILE-"),
            sg.FileBrowse(file_types=file_types),
            sg.Button("Load Image"),
        ],
    ]
    window = sg.Window("Projekt - Analiza Obrazów", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Load Image":
            filename = values["-FILE-"]
            if os.path.exists(filename):
                window["-IMAGE-"].update(filename=values["-FILE-"])


    window.close()
if __name__ == "__main__":
    main()