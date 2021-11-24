import pttsx3
import spech_recognition as sr
import webbrowser
import datetime
import pywhatkit
import os
import yfinannce as yf
import pyjokes

#Listen to the microphone and return the audio as text using Google

def transform():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold =0.8
        said = r.listen(source)
        try:
            print ('I am lsitening')
            q = r.recognize_google(said, language = "en")
            return q
        except sr.UnknwnValueError:
            print("Sorry I did not cach that")
            return "I am waiting"
        except sr.RequestError:
            print ('Sorry milord, service is down')
            return "I am waiting"
        except:
            return "I am waiting"
        
def speaking(message):
        engine = pyttsx3.init()
        engine.say(message)
        engine.runAndWait()
        
        engine = pyttsx3.init()
        for voice in engine.getProperty('voices'):
        
        id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\TOkens\TTS_MS_EN_US_ZIRA_11.0'
        engine.setPorperty('voice',id)
        engine.say ('Hello world')
        engine.runAndWait()

#Returns the weekday name
def query_day():
    day = datetime.date.today89
    print(day)
    weekday = day.weekday()
    print(weekday)
    mapping = {
        0: 'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'
    }
    try:
        speaking(f'today is{mapping[weekday]}')
    except:
        pass

query_day()

#Returns the time
def query_time():
    time=datetime.datetime.now().strftime("%I:%M:%S")
    speaking(f"{time[1]} o'clock and {time[3:5]} minutes")
    
query_time()

#Intro greeting at startup. Thyra is a female name in norse/icelandic that means helpfull
def greetings():
    speaking('''Greetings, my name Thyra. I am your personal assistant.
    How may I help you
             ''')
    
greetings()
    