import os
import webbrowser
import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
print(hii i am tegveer singh)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate',180)
#print(rate)
#print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



now = datetime.datetime.today()
#print(now)
#speak(now)


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
if __name__ == '__main__':
    speak("Hello sir i am Veronica, your personal study companiyan")
    speak("please tell what can i do for you sir..")
    speak("i am Listening...")
    while True:
        query = takeCommand().lower()
        if 'wake up' in query:
            speak('I am up sir')
        elif 'wikipedia' in query:
            speak('Searching Wikipedia..')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open("youtube.com")
        elif 'open drive' in query:
            speak('opening your drive')
            webbrowser.open("https://drive.google.com/drive/u/1/my-drive")
        elif 'time' in query:
            speak('the time is')
            speak(now)
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
        elif 'good' in query:
            speak("Thank you sir,its my pleasure. any thing else")
        elif 'play music' in query:
            speak('playing music')
            from playsound import playsound
            playsound('C:/Users/pragati computers/Desktop/tegveer/Dil_Meri_Na_Sune_Lyrical_-_Genius__Utkarsh,_Ishita__Atif_Aslam__Himesh_Reshammiya__Manoj(128kbps).mp3')
        elif 'open vs code' in query:
            speak('opening v s code')
            codePath = "C:\\Program Files (x86)\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open PyCharm' in query:
            speak('opening PyCharm')
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.2\\bin\\pycharm64.exe"
            os.startfile(codePath)
        elif 'open blender' in query:
            speak('opening blender')
            codePath = "C:\\Program Files\\Blender Foundation\\Blender\\blender.exe"
            os.startfile(codePath)
        elif 'open game' in query:
            speak('opening your game')
            codePath = "C:\\Program Files\\Desert Storm\\DesertStorm.exe"
            os.startfile(codePath)
        elif 'open notepad' in query:
            speak('opening notepad')
            codePath = "C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
            os.startfile(codePath)
        elif 'open atom' in query:
            speak('opening atom')
            codePath = "C:\\Users\\pragati computers\\AppData\\Local\\atom\\atom.exe"
            os.startfile(codePath)
        elif 'movie' in query:
            speak('let me show you some movie sir')
            codePath = "C:\\Users\\pragati computers\\Desktop\\tegveer\\Jurassic World_ Fallen Kingdom_640P.mp4"
            os.startfile(codePath)
        else:
            print("exit")
else:
    print("progaram exit")
