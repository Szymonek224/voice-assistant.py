import pyttsx3
import webbrowser
import os
import speech_recognition as sr
import time
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
wb = webbrowser
engine.say("please speak")
engine.runAndWait()
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said
loop = False 
def commands():
    text = get_audio()
    match text:
        case "bread":
            engine.say("I put on a song")
            engine.runAndWait()
            wb.open('https://youtu.be/UTFP6YTYgIQ')
        case "open YouTube":
            engine.say("I turn on youtube")
            engine.runAndWait()
            wb.open('https://www.youtube.com')
        case "open Google" :
            engine.say("I turn on google")
            engine.runAndWait()
            wb.open('https://www.google.com')
        case "sing" :
            engine.say("Twinkle, twinkle, little star,How I wonder what you are!Up above the world so high,Like a diamond in the sky.")
            engine.runAndWait()
        case "open something":
            engine.say("what should i enable?")
            engine.runAndWait()
            turnOn = input("give me the link")
            engine.say("I turn on"+turnOn)
            engine.runAndWait()
            wb.open_new_tab(str(turnOn))
        case "open spotify":
            engine.say("I turn on spotify")
            engine.runAndWait()
            wb.open('https://www.spotify.com/pl/https://www.spotify.com/pl/')
        case "open relaxing music":
            engine.say("I turn on relaxing music")
            engine.runAndWait()
            wb.open('https://www.youtube.com/watch?v=erNvMS9-tto')
        case"turn on the light":
            engine.say("I turn on the light")
            engine.runAndWait()
            wb.open('https://d.allegroimg.com/original/12983c/c2dc05ea4c6b91ff0a1241121ead')
        case "turn off the light":
            engine.say("I turn off the light")
            engine.runAndWait()
            os.system("shutdown /s /t 1")
        case"kill yourself":
            engine.say("I am killing yourself")
            engine.runAndWait()
            exit()
        case "I love you":
            engine.say("unfortunately, I don't have a built-in module for feeling feelings, but I can say that I love you too")
            engine.runAndWait()
        case other:
            engine.say("Sorry, I don't understand but maybe you'll like it")
            engine.runAndWait()
            wb.open(text)
            time.sleep(1)
            engine.say("if not, repeat the command")
            time.sleep(1)
            global loop
            loop = True
def orders():
    commands()
    

    while loop == True:
        commands()
orders()
