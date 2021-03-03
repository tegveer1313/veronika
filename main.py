import os
import webbrowser
from datetime import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
from googlesearch import search
import smtplib
import bluetooth
import pywifi
import time
from pywifi import const
import speedtest
import pyautogui
import psutil
import randfacts
#This is python text to speach.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate',180)
#you can change voice according to you by changing the number in voice[].
engine.setProperty('voice', voices[3].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#This is to define date and time.
def wish_me():
    now = datetime.now()
    hours = int(now.strftime("%H"))
    minn = now.strftime("%M")
    sec = now.strftime("%S")

    if hours >= 0 and hours < 12:
        speak(f"its {hours} {minn} AM")
    elif hours >= 12 and hours < 24 :
        speak(f"its {hours} {minn} PM")

    if hours >= 0 and hours < 12 :
        speak("Good Moring sir")
    elif hours >= 12 and hours < 18 :
        speak("Good afternoon sir")
    elif hours >= 18 :
        speak("Good evening sir")
        
#defineing takeCommand fn. it will recognize user audio input. 
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        # print(e)
        print("say that again please... OR cheak your internet ")
        return 'none'
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    speak("I need you email and its password, sir enter them below")
    send_to2 = input("Enter your Email:- ")
    word = (input("Enter your password:- "))
    server.login(send_to2, word)
    server.sendmail(send_to2, to, content)
    server.close()
if __name__ == '__main__':
    name = "Tegveer Singh"
    wish_me()
    speak("i am Veronica.")
    speak("please tell what can i do for you sir..")
    speak("i am Listening...")
    while True:
        query = takeCommand().lower()
        #You should change the links,URLsand file location according to you. 
        if 'wake up' in query:
            speak('I am up sir')
        if 'fact' in query:
            x = randfacts.getFact()
            speak(x)
        elif 'wikipedia' in query:
            speak('Searching Wikipedia..')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open("youtube.com")
        elif 'search' in query:
             speak('sir,  what should i search')
             cm = takeCommand().lower()
             speak('heres what i found')
             webbrowser.open(f"{cm}")
        elif 'link' in query:
            speak('What do you want to search..')
            query = takeCommand().lower()
            speak('Searching google..')
            speak('I found 5 results')
            for i in search(query, tld="com", num=5, stop=5, pause=2):
                print(i)
                speak(i)
        elif 'open drive' in query:
            speak('opening your drive')
            webbrowser.open("https://drive.google.com/drive/u/1/my-drive")
        elif 'time' in query:
            speak("yes sir")
            now = datetime.now()
            hours = int(now.strftime("%H"))
            minn = now.strftime("%M")
            sec = now.strftime("%S")

            if hours >= 0 and hours < 12:
                speak(f"its {hours} {minn} AM")
            elif hours >= 12 and hours < 24 :
                speak(f"its {hours} {minn} PM")
            else :
                speak("sorry sir i am not able to tell it now.")
        elif 'battery' in query:
            speak('checking battery status')
            battery = psutil.sensors_battery()
            battery_per = battery.percent
            speak(f"your battery is {battery_per} percent charged")
            if battery_per <= 50:
                speak(f"your battery percent is {battery_per}. it is low plese plug in charger")
        elif 'internet speed' in query:
            speak("testing internet speed")
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            dl2 = dl * 0.000001
            up2 = up * 0.000001
            speak(f"sir we have {dl2} mb per second downloading speed and {up2} mb per second upload ing speed")
        elif 'open my channel' in query:
            speak('opening your channel')
            webbrowser.open("https://www.youtube.com/channel/UCXeDwy9_kgTjo3tyFY9E7Tw?view_as=subscriber")
        elif 'open chess' in query:
            speak('opening chess')
            webbrowser.open("https://www.youtube.com/channel/UCeg7zY285sTls-uyzBDLfYw")
        elif 'open google' in query:
            speak('opening google')
            webbrowser.open("google.com")
        elif 'who created you veronica' in query:
            speak("Tegveer singh had created me. he is my god")
        elif 'bluetooth' in query:
            speak("yes sir searching bluetooth")
            nearby_devices = bluetooth.discover_devices(lookup_names=True)
            print("Found {} devices.".format(len(nearby_devices)))
            speak("Found {} devices nearby".format(len(nearby_devices)))
            if nearby_devices == []:
                speak("sir please check weather your bluetooth is on or not.")    
            speak("here are the devices what i found")
            for addr, name in nearby_devices:
                print("{}".format(name))
                speak("{}".format(name))
        elif 'wi-fi' in query:
            speak("yes sir searching wifi")
            wifi = pywifi.PyWiFi()

            Iface = wifi.interfaces()[0]
            name = Iface.name()
            Iface.scan()
            time.sleep(1)

            results = Iface.scan_results()
            for data in results:
                print(data.ssid)
                speak(data.ssid)
        elif "what's my name" in query:
            speak(name)
            ans = takeCommand().lower()
            if "no" in ans:
                speak("oh! sorry sir whats your name tell me i will remember it for future")
                name = takeCommand().lower()
            else:
                speak("Something went wrong")
        elif 'what can you do for me' in query:
            speak("Hii sir i can write Emails and send them, i can search on google, play music, dont worry if you got bored i can even play moives for you and many more")
        elif 'good' in query:
            speak("Thank you sir,its my pleasure. any thing else")
        elif 'screenshot' in query:
            speak("sir please tell me the name of this screenshot file")
            h = takeCommand().lower()
            speak("sir please hold the screen for few second, i am taking screenshot")
            img = pyautogui.screenshot()
            img.save(f'{h}.png')
        elif 'play music' in query:
            speak('playing music')
            from playsound import playsound
            playsound('E:/VIDEO & MP3&WALLPAPER/A.R.RAHMAN/TU HI RE')
        elif 'open vs code' in query:
            speak('opening v s code')
            codePath = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open blender' in query:
            speak('opening blender')
            codePath = "C:\\Program Files\\Blender Foundation\\Blender 2.91\\blender.exe"
            os.startfile(codePath)
        elif 'movie' in query:
            speak('let me show you some movie sir')
            codePath = "E:\VIDEO & MP3&WALLPAPER\Video full hd\Mere Wala Sardar (Full Song)  _ Jugraj Sandhu  _ New Song 2018 _ New Punjabi Songs 2018"
            os.startfile(codePath)
        elif 'send email' in query:
            speak("Sir enter below To whom do you want to send Email  ")
            send_to = input("To whom do you want to send Email:- ")
            try:
                speak('What should I say')
                content = takeCommand()
                to = send_to
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir i am not able to sent Email right now.")
        else:
            print("exit")
else:
    print("progaram exit")