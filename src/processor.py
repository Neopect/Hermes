# Processor.py - Handles system sub modules for processing requests

import datetime
import time

import scheduler as shed
import inListener

import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config

if __name__=='__main__':
    

    statement = inListener.takeCommand().lower()
    
   # if statement==0:
        #continue

    #if 

    
def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]


def dateTranslator(text, digit):
    dt_now = datetime.datetime.now()
    dt_new = None

    #Find date "in x days"
    if any(char.isdigit() for char in text):
        dt_split = text.split()
        val = int()
        
        for word in dt_split:
            try:
                val = int(word)
            except ValueError:
                pass
        
        dt_change = datetime.timedelta(days=val)
        dt_new = dt_now + dt_change
        
        
    if text.contains("today"):
        dt_new = dt_now
    elif text.contains("tomorrow"):
        dt_change = datetime.timedelta(days=1)
        dt_new = dt_now + dt_change
    
    return dt_new


def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results