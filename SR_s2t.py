import PySimpleGUI as sg
from datetime import datetime, time

import speech_recognition as sr
import keyboard
import pyaudio
import wave


audio = pyaudio.PyAudio()
WAVE_OUTPUT_FILENAME = "output.wav"

beginning_of_prog = datetime.now() 

layout = [[sg.Text('Recording Time: '), sg.Text('', key='_time_', size=(10, 1))],
         [sg.Text(' '*17), sg.Quit()]]

window = sg.Window('Simple Clock').Layout(layout)

def getTime():
    
    now = datetime.now()
     
    return(now - beginning_of_prog).seconds

def main(gui_obj):

    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    
    audio = pyaudio.PyAudio()
    WAVE_OUTPUT_FILENAME = "output.wav"

    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    print ("recording...")
    frames = []

    while True:

        event, values = gui_obj.Read(timeout=10)

        gui_obj.FindElement('_time_').Update(getTime())

        data = stream.read(CHUNK)
        frames.append(data)

        if event in (None, 'Quit'):

            print ("finished recording")
             
             
            # stop Recording
            stream.stop_stream()
            stream.close()
            audio.terminate()
             
            waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
            waveFile.setnchannels(CHANNELS)
            waveFile.setsampwidth(audio.get_sample_size(FORMAT))
            waveFile.setframerate(RATE)
            waveFile.writeframes(b''.join(frames))
            waveFile.close()

              
            AUDIO_FILE = ("output.wav") 
              
            # use the audio file as the audio source 
              
            r = sr.Recognizer() 
              
            with sr.AudioFile(AUDIO_FILE) as source: 
                #reads the audio file. Here we use record instead of 
                #listen 
                audio = r.record(source)   
              
            try:
                datastr=r.recognize_google(audio)
                print(datastr) 
              
            except sr.UnknownValueError: 
                print("Speech Recognition could not understand audio")
                datastr="Speech Recognition could not understand audio"
              
            except sr.RequestError as e: 
                print("Could not request results from Speech Recognition service; {0}".format(e)) 
                datastr="Could not request results from Speech Recognition service"
            finally:
                with open('s2t.txt','w+') as ff:
                    ff.write(datastr)
                
                break
            
      
    window.close()
    
if __name__ == '__main__':
    main(window)
