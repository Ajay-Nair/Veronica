
#for speech engine
import pyttsx3
from decouple import config

#for greet
from datetime import datetime

#for speech recog
import speech_recognition as sr
from random import choice
from utils import opening_text

#importing functions
from functions.online_fn import find_my_ip,send_email

from functions.os_fn import open_calc,open_cmd,open_discord,open_camera



#Taking user input using speech recog
def user_input():
    #takes input and converts it to text using speech recognition

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio,language='en-in')
        if not 'exit' in query or not 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if( hour>=21 and hour<6):
                speak(f"Good night sir")
            else:
                speak("See ya boss.")
            exit()
    except Exception:
        speak('Sorry,I could not understand . Please say that again.')
        query='None'
    return query




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
    elif( hour>=17 and hour<23):
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

if __name__ == "__main__":
    greet()
    while(True):
        query = user_input().lower()
        print(query)
        if 'ip' in query:                               #find ip address
            print(find_my_ip())
        elif 'camera' in query:                         #open camera
            open_camera()
        elif 'email' in query:                          #open email
            speak("Enter the subject")
            subject = input()
            speak("Enter the body")
            body = input()
            speak("Enter the recieving email")
            reciever = input()
            send_email(subject,body,reciever)

        

