# This is my version of JARVIS

# Imports
import os
import speech_recognition as sr
import playsound
import time
import datetime
from gtts import gTTS
from os import path

# Functions
def speak(text):
    tts = gTTS(text=text, lang='en', tld ='co.uk')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said.lower())
        except Exception as e:
            print("Waiting: " + str(e))
    return said.lower()

def setup():
    hour = int(datetime.datetime.now().hour)
    speak("Welcome Sir")
    if hour>= 0 and hour<12:
        speak("Good Morning!")

    elif hour>= 12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    speak("I am your Assistant")
    speak("Jarvis")

def get_name():
    speak("What is your name sir?")
    usrname = get_audio()
    return usrname

def rid_repeats():
    f = open("queue.txt", "w")
    lines_seen = set()
    for line in open("queue.txt", "r"):
        if line not in lines_seen:
            f.write(line)
            lines_seen.add(line)
    f.close()

def check_queue(task):
    file = path.isfile('queue.txt')
    if file is True:
        f = open("queue.txt", "a")
        f.write(task + "\n")
        #rid_repeats()
        speak("This task will be added to my library")
    else:
        speak("False")

# Main function starts here
if __name__ == '__main__':
    #setup()
    #usrname = get_name()
    #speak("How can I assist you" + usrname)
    while True:
        command = get_audio()
        if "jarvis" in command:
            # These are the commannds JARVIS can respond to
            if "hello" in command:
                speak("hello")

            else:
                check_queue(command)
