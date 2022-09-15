# Text interrupter

from decouple import config
from datetime import datetime
from random import choice
from utils import opening_text

USERNAME = config('USERN')
BOTNAME = config('BOTNAME')

class cliProcessor(): 

    # Greet the user
    def greet_user(self):
        """Greets the user according to the time"""
        
        hour = datetime.now().hour
        if (hour >= 6) and (hour < 12):
            print(f"Good Morning {USERNAME}")
        elif (hour >= 12) and (hour < 16):
            print(f"Good afternoon {USERNAME}")
        elif (hour >= 16) and (hour < 19):
            print(f"Good Evening {USERNAME}")
        print(f"I am {BOTNAME}. How may I assist you?")


    # Takes Input from User
    def take_user_input(self):
        """Takes user input, recognizes it using Speech Recognition module and converts it into text"""
        
        try:
            print('Recognizing...')
            query = input('> ')
            if not 'exit' in query or 'stop' in query:
                print(choice(opening_text))
            else:
                hour = datetime.now().hour
                if hour >= 21 and hour < 6:
                    print("Good night sir, take care!")
                else:
                    print('Have a good day sir!')
                exit()
        except Exception:
            print('Sorry, I could not understand. Could you please say that again?')
            query = 'None'
        return query

