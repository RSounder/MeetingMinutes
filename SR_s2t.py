import PySimpleGUI as sg
from datetime import datetime, time

beginning_of_prog = datetime.now() 

layout = [[sg.Text('Recording Time: '), sg.Text('', key='_time_', size=(10, 1))],
         [sg.Text(' '*17), sg.Quit()]]

window = sg.Window('Simple Clock').Layout(layout)

def getTime():
    

    now = datetime.now()
     
    return(now - beginning_of_prog).seconds

def main(gui_obj):
    while True:
        event, values = gui_obj.Read(timeout=10)

        if event in (None, 'Quit'):
            break

        gui_obj.FindElement('_time_').Update(getTime())

    window.close()
    
if __name__ == '__main__':
    main(window)
