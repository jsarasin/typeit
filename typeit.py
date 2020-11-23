#!/usr/bin/python3

import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()


with mic as source:
    audio = r.listen(source)
    print(r.recognize_sphinx(audio))
