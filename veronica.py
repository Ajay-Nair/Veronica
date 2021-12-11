
#for speech engine
import pyttsx3
from decouple import config

#for greet
from datetime import datetime

#text to speech conversion
def speak(text):
    #speaks text which is passed
    engine.say(text)
    engine.runAndWait()

#Greet function
def greet():
    hour = datetime.now().hour
    if( hour>=5 and hour<12):
        speak(f"Good morning {USERNAME} . I am {BOTNAME} , How may I assist you? ")
    elif( hour>=12 and hour<17):
        speak(f"Good afternoon {USERNAME} . I am {BOTNAME} How may I assist you?")
    elif( hour>=17 and hour<21):
        speak(f"Good evening {USERNAME} . I am {BOTNAME} ,How may I assist you?")
    else:
        speak("Do you know what time it is ? Do it yourself!")


#Creating a speech engine

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init('sapi5') #Object Creation

#Set rate
engine.setProperty('rate',190)

#set volume
engine.setProperty('volume',1)      #value of vol between 0 and 1

#set voic
voices = engine.getProperty('voices')   #gets list of voices
engine.setProperty('voice',voices[1].id) # 0 for male

greet()
