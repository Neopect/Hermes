# Listener.py - Takes and processes input

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk
import json
import speech_recognition as sr
import pyttsx3
import datetime
import requests

engine=pyttsx3.init()
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


def breakdown(phrase, lemmatize = True):
    # Takes input and parses through nltk then outputs the parsed phrase with lemitizing depending on pram.

    grammar = "NP: {<DT>?<JJ>*<NN>}"

    phrase_words = word_tokenize(phrase)
    
    if lemmatize == True:
        lemmatizer = WordNetLemmatizer()
        phrase_lemma = [lemmatizer.lemmatize(word) for word in phrase_words] # LATER Ensure words follow proper grammar types
    else:
        phrase_lemma = phrase_words

    phrase_tags = nltk.pos_tag(phrase_lemma)
    chunk_parser = nltk.RegexpParser(grammar)
    phrase_parsed = chunk_parser.parse(phrase_tags)

    return phrase_parsed

test = breakdown("What is the weather in 2 days?")
print(test)
print(test[0])
print(test[1])
print(test[0][0])
print(test[0][0][0])

