#!/usr/bin/python3
import pyaudio
import speech_recognition as sr
from pyautogui import press, typewrite, hotkey

r = sr.Recognizer()
print("caat" + pyaudio.get_device_count())

mic = sr.Microphone(0)

while 1:
    print("sdf");
    with mic as source:
        print("ct");
        audio = r.listen(source)
        typewrite(r.recognize_google(audio) + "\n\r")
        # typewrite(r.recognize_sphinx(audio) + "\n\r")
