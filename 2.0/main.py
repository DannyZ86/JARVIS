# This is my version of JARVIS

# Imports
import os
import speech_recognition as sr
import playsound
from gtts import gTTS

# Functions
def speak(text):
    tts = gTTS(text=text, lang='en', tld ='co.uk')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said

# Main function starts here
if __name__ == '__main__':
    text = get_audio()

    if "hello" in text:
        speak("hello, how are you?")
    elif "what is your name" in text:
        speak("My name is JARVIS")
    else:
        speak("I do not understand this question yet")
        f = open("queue.txt", "a")
        f.write(text)
        f.close()
