# Listener.py - Takes and processes input

import json
import speech_recognition as sr
import pyttsx3

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

# Makes TTS speak to user
def speak(msg):
    engine.say(msg)
    engine.runAndWait()

# Greets user based on conditions
def greetMe():
    pass

# def vocal():
#     pass

def deconstructor(input):
    pass

# Processes command
def takeCommand(inputType = 'string'):

    if inputType == 'string':
        statement = input(': ')
        print(f'Processing request for \"{statement}\"') 
        return statement
    

    elif inputType == 'vocal':
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio=r.listen(source)

            try:
                statement=r.recognize_google(audio,language='en-in')
                print(f"user said:{statement}\n")

            except Exception as e:
                speak("Pardon me, please say that again")
                return "None"
            return statement