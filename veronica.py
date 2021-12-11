#Creating a speech engine
import pyttsx3
from decouple import config

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

