# packeges istall for this project:
# pip install SpeechRecognition
# pip install pipwin
# pipwin install pyaudio
# pip install pywhatkit

import speech_recognition as sr
import pyaudio
import pywhatkit
import os
import webbrowser


lis = sr.Recognizer()

with sr.Microphone() as source:
    print("Listen...")
    voice = lis.listen(source)
    command = lis.recognize_google((voice))
    command = command.lower()
    print("*****", command, "*****")

    if("computer") in command:
        command = command.replace("computer", "")
        # open dirctly video
        # if("play") in command:
        #     command = command.replace("play", "")
        #     pywhatkit.playonyt(command)

        # notepad
        if ("one") in command:
            os.system("notepad")
        # youtube
        if("youtube") in command:
            command = command.replace("youtube", "")
            if("look") in command:  # ـنصق lk
                command = command.replace("look", "")
                print("command=", command)
                webbrowser.open(
                    "https://www.youtube.com/results?search_query="+command)
            else:
                print("sle")
                webbrowser.open("https://www.youtube.com")
                # webbrowser.open(
                # "https://www.youtube.com"/results?search_query="+command")
        if("google") in command:
            command = command.replace("youtube", "")
            if("look") in command:  # ـنصق lk
                command = command.replace("look", "")
                print("command=", command)
                webbrowser.open(
                    "https://www.google.com/search?q="+command+"&oq=&aqs=chrome.0.69i59i450l8.374100734j0j15&sourceid=chrome&ie=UTF-8")
            else:
                webbrowser.open("https://www.google.com")

        print("yes")
