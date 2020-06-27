import PySimpleGUI as sg
import datetime
import time
import os
import keyboard

today = datetime.date.today()
d1 = today.strftime("%b_%d_%Y")

def append_file(file_name, lines_to_append):
    
    with open(file_name, "a+") as file_object:
        appendEOL = False
        # Move read cursor to the start of file.
        file_object.seek(0)
        # Check if file is not empty
        data = file_object.read(100)
        if len(data) > 0:
            appendEOL = True
        # Iterate over each string in the list
        for line in lines_to_append:

            if appendEOL == True:
                file_object.write("\n")
            else:
                appendEOL = True
            # Append element at the end of file
            file_object.write(line)

theme_dict = {'BACKGROUND': '#2B475D',
                'TEXT': '#FFFFFF',
                'INPUT': '#F2EFE8',
                'TEXT_INPUT': '#000000',
                'SCROLL': '#F2EFE8',
                'BUTTON': ('#000000', '#C2D4D8'),
                'PROGRESS': ('#FFFFFF', '#C7D5E0'),
                'BORDER': 1,'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0}

sg.LOOK_AND_FEEL_TABLE['Dashboard'] = theme_dict
sg.theme('Dashboard')

BORDER_COLOR = '#C7D5E0'
BORDER_COLOR2 = '#787b80'

DARK_HEADER_COLOR = '#1B2838'
BPAD_TOP = ((20,20), (20, 10))
BPAD_LEFT = ((20,10), (0, 10))
BPAD_LEFT_INSIDE = (0, 10)
BPAD_LEFT2_INSIDE = (20, 10)
BPAD_RIGHT = ((10,20), (10, 20))
BPAD_BOTTOM = (100,0)

d2 = today.strftime("%A, %b-%d-%Y  ")
timenow = now = datetime.datetime.now()

top_banner = [[sg.Text('Minute-inator'+ ' '*50, font='Any 20', background_color=DARK_HEADER_COLOR),
               sg.Text(d2, font='Any 20', background_color=DARK_HEADER_COLOR), sg.Button(' X ')]]

clubname = "RaC Spectrum"
clubid = "92268"
rid = "3201"
chair = "Rtr. Name"
minsby = "Rtr. Name2"
attnlis = ["Rtr. Name1" , "Rtr. Name8", "Rtr. Name7", "Rtr. Name6", "Rtr. Name5", "Rtr. Name4", "Rtr. Name3", "Rtr. Name2"]
meetname = "Meeting Name Here"

file_name = 'Minutes of ' + meetname + ' ' + today.strftime("%B_%d_%Y")+'.txt'


detailstr = 'Host Club: ' + clubname + ' | Club ID: ' + clubid + ' | RID: ' + rid + ' | Chair: ' + chair + ' | Minutes by: ' + minsby

top  = [[sg.Text('Meeting Name here', size=(50,1), justification='c', pad=BPAD_TOP, font='Any 20')],
            [sg.Text(detailstr, size=(100,1), justification='c',  font='Any 10')], ]

block_2 = [[sg.Text('Auto Transcribe', font='Any 15')],
            [sg.Text('Speaker:', size = (10,1)), sg.InputCombo(values = attnlis, size=(20, 1),key='aspker'),sg.Button('Start Recording')] ,
            [sg.Text('', size = (10,1)),sg.Multiline(' ', size = (40,3), key ='autospeech')  ],[sg.Text(' ', size = (35,1)),sg.Button('Commit'),sg.Button('Enter')]]


block_3 = [[sg.Text('Manual Minutes', font='Any 15')],
            [sg.Text('Speaker:',size = (10,1)), sg.InputCombo(values = attnlis, size=(20, 1),key='manspker')],
            [sg.Text('Points:', size = (10,1)), sg.Multiline(size=(40,3), key='manspeech')],[sg.Text(' ', size = (37,1)), sg.Button('Manual Enter')]]

block_4 = [[sg.Text('Add Attendees', font='Any 15')],[sg.Text('Name:', size = (5,1)), sg.Input(size=(18,1),key='addattn')],[sg.Text(' ', size = (18,1)), sg.Button('Add',key='addattnbut')]]
block_6 = [[sg.Text('Status Console', font='Any 15')],[sg.Text('Status: Initialised', size = (25,1),key='cons1')],[sg.Multiline('', size = (25,4),key='cons2')]]

block_5 = [[sg.Text('Text to PDF', font='Any 15')],
            [sg.T('Select the .txt file to be converted to pdf')],
            [sg.Input(), sg.FileBrowse()],
            [sg.Text(' ', size = (32,1)), sg.Button('Convert')]]

layout = [[sg.Column(top_banner, size=(960, 60), pad=(0,0), background_color=DARK_HEADER_COLOR)],
          [sg.Column(top, size=(910, 90), pad=BPAD_TOP)],
          [sg.Column([[sg.Column(block_2, size=(440,160), pad=BPAD_LEFT_INSIDE)],
                      [sg.Column(block_3, size=(440,160),  pad=BPAD_LEFT_INSIDE)]], pad=BPAD_LEFT, background_color=BORDER_COLOR),
           sg.Column([[sg.Column(block_4, size=(210,160), pad=BPAD_LEFT_INSIDE),sg.Column(block_6, size=(210,160), pad=BPAD_LEFT2_INSIDE)],
                      [sg.Column(block_5, size=(440,160),  pad=BPAD_LEFT_INSIDE)]], pad=BPAD_LEFT, background_color=BORDER_COLOR),
           ]]

window = sg.Window('Dashboard PySimpleGUI-Style', layout, margins=(0,0), background_color=BORDER_COLOR, no_titlebar=True, grab_anywhere=True)

try:
    today = datetime.date.today()
    d1 = today.strftime("%b_%d_%Y")
    os.mkdir('files_' + d1)
    print(str(d1) + ' Folder Created')
except:
    print(str(d1) + ' Folder Exists')


while True:

    # Event Loop
    timenow1 = time.strftime("%H:%M:%S")    
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == ' X ':
        break
        
    if event == 'Start Recording':
        window.Element('cons1').Update('Recording Starts')
        os.system('python SR_s2t.py')
        #cwd = os.getcwd()
        #print(cwd)
        pass

    if event == 'Enter':
        #manual writing of text from text box
        window.Element('cons1').Update('Auto Enter Pressed')
        li = [values['aspker'] + ' at ' + str(timenow1) + ': ', values['autospeech']] 
        append_file(file_name, li)
        pass
        
    if event == 'Manual Enter':
        #manual writing of text from text box
        window.Element('cons1').Update('Manual Enter Pressed')
        li = [values['manspker'] + ' at ' + str(timenow1) + ': ', values['manspeech']] 
        append_file(file_name, li)
        pass

    if event == 'Commit':
        #publishing text from s2t.txt to multiline
        with open('s2t.txt') as ff:
            datastr = ff.read()
        window.Element('autospeech').Update(datastr)
        pass
    
    if event == 'addattnbut':
        #add attends
        window.Element('cons1').Update('Added' + ' ' + values['addattn'])

        attnlis.append(values['addattn'])
        attnset=set(attnlis)
        attnlis=list(attnset)
        
        window.Element('manspker').Update(values = attnlis)
        window.Element('aspker').Update(values = attnlis)
        
        pass

print("Closing Application")
window.close()
