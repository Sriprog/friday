import datetime
import os
import webbrowser
import random

import pyttsx3
import speech_recognition as sr
import wikipedia
import pyaudio
import smtplib
import pyjokes
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif (hour >= 12 and hour < 18):
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    speak("I am friday. Your Personal Assistant. Ready to roll!!")


def takeCommand():
    '''Takes the microphone input as a string '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("")
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 700
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        # print(e)

        # print("I didn't catch you BOSS. Say it again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('srinivaslooter@gmail.com', 'SR@$$inu8647')
    server.sendmail('srinivaslooter@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # Logic for executing tasks based on query

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("Opening google")
            webbrowser.open("google.com")
        elif 'open stackover' in query:
            speak("opening Stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'open facebook' in query:
            speak("Opening Facebook")
            webbrowser.open("facebook.com")
        elif 'open github' in query:
            speak("Opening Github")
            webbrowser.open("github.com")
        elif 'play music' in query:
            music_dir = 'E:\\Music\\songs'
            songs = os.listdir(music_dir)
            num = random.randint(0, len(songs))
            speak("Playing Music!!")
            os.startfile(os.path.join(music_dir, songs[num]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")

        elif 'open code' in query:
            vscodePath = "C:\\Users\\Universe\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("opening VS Code")
            os.startfile(vscodePath)

        elif 'open word' in query:
            wordPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            speak("opening MS Word!!")
            os.startfile(wordPath)

        elif 'open speed' in query:
            speak("opening speedtest")
            webbrowser.open("fast.com")

        elif 'open chrome' in query:
            chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            speak("Opening Chrome")
            os.startfile(chromePath)

        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("spotify.com")

        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "muddanasaraswati@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!!")
            except Exception as e:
                print(e)
                speak("Sorry sir Email not sent")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "kill" in query:
            speak("killing friday")
            exit()
