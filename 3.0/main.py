import json
import speech_recognition as sr
import playsound
import os
import random
from os import path
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('wLUZQI_w70b07i9xZtgGd5cqdQ9nOlxGjUpbnO4eOhpp')
service = SpeechToTextV1(authenticator = authenticator)

service.set_service_url('https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/8267b79a-00ac-4961-9d21-4005efb122c1')

filename = "ibmvoice.mp3"

with open(join(dirname(filename), r'C:\Users\Danny\JARVIS\3.0'),
          'rb') as audio_file:

        dic = json.loads(
                json.dumps(
                    service.recognize(
                        audio=audio_file,
                        content_type='audio/flac',
                        model='en-GB_JamesV3Voice',
                    continuous=True).get_result(), indent=2))
str = ""

while bool(dic.get('results')):
    str = dic.get('results').pop().get('alternatives').pop().get('transcript')+str[:]

print(str)
