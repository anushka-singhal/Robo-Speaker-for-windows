import os
import win32com.client as wincom
print("Welcome to RoboSpeaker")
while True:
    text = input("Enter what you want me to pronounce")
    if text == "stop":
         break
    speak = wincom.Dispatch("SAPI.SpVoice")
    speak.Speak(text)


 