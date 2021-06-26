import datetime
import os
import webbrowser
import random

import requests
from bs4 import BeautifulSoup
from googletrans import Translator
from playsound import playsound
import pyautogui

from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Tk
from tkinter import StringVar
from pytube import YouTube
from PyDictionary import PyDictionary as Dictionary
from pywikihow import search_wikihow
from gtts import gTTS
import keyboard
import pyttsx3
import pywhatkit as pywhatkit
import speech_recognition as sr
import wikipedia
import whatsapp
import smtplib
import pyjokes
import PyPDF2

friday = pyttsx3.init('sapi5')
voices = friday.getProperty('voices')
friday.setProperty('voice', voices[3].id)
friday.setProperty('volume',100)
friday.setProperty('rate',170)

def speak(audio):
    print("..................")
    friday.say(audio)
    print(f"Friday:{audio}")
    friday.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")


    elif (hour >= 12 and hour < 18):
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("I am friday. Your Personal Assistant. Lets rock and roll")
    speak("What can I do For you")

def takeCommand():
    '''Takes the microphone input as a string '''
    r = sr.Recognizer()
    with sr.Microphone() as source:

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

        speak("I didn't catch you BOSS. Say it again please...")
        return "None"
    return query

def Trans():
    speak("Tell me the Line!")
    translater = Translator()
    line = takeCommand()
    trans = translater.translate(line,dest='te')
    print(trans.text)
    speak(trans.text)

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('srinivaslooter@gmail.com', 'SR@$$inu8647')
    server.sendmail('srinivaslooter@gmail.com', to, content)
    server.close()

def Whatsapp():
    speak("To whom should i dm?")
    name = takeCommand()
    if 'amma' in name:
        speak("What should i send")
        msg = takeCommand()
        speak("On what time Boss. specify in hour")
        hr = int(takeCommand())
        speak("specify in min")
        min = int(takeCommand())
        pywhatkit.sendwhatmsg("7794897284", msg, hr,min, 20)
        speak("Ok boss, Sending whatsapp Message!")

    else:
        speak("specify phone number ")
        ph = takeCommand()
        phone_number = "+91" + ph
        speak("msg that i should dm")
        msg = takeCommand()
        speak("On what time Boss. specify in hour")
        hr = int(takeCommand())
        speak("specify in min")
        min = int(takeCommand())
        pywhatkit.sendwhatmsg(phone_number, msg, hr, min, 20)
        speak("Ok boss, Sending whatsapp Message!")

def OpenApps():
    speak("Ok boss, getting it from stark cloud!!")
    if 'open youtube' in query:
        speak("Opening youtube Boss")
        webbrowser.open("youtube.com")


    elif 'open google' in query:
        speak("Opening google")
        webbrowser.open("google.com")

    elif 'open facebook' in query:
        speak("Opening Facebook")
        webbrowser.open("facebook.com")

    elif 'open github' in query:
        speak("Opening Github")
        webbrowser.open("github.com")

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
    speak("Your command is cooked and served.")

def CloseApp():
    speak("Ok boss,Wait a second!!")

    if 'chrome' in query:
        os.system("TASKKILL /F /im chrome.exe")

    if 'music' in query:
        os.system("TASKKILL /F /im Music.UI.exe")

def YoutubeAuto():
    speak("Whats Your Command?")
    comm = takeCommand()
    if 'pause' in comm:
        keyboard.press("space bar")

    elif 'restart' in comm:
        keyboard.press("0")

    elif 'mute' in comm:
        keyboard.press("m")

    elif 'skip' in comm:
        keyboard.press('l')

    elif 'back' in comm:
        keyboard.press('j')

    elif 'full screen' in comm:
        keyboard.press('f')

    elif 'Theater mode' in comm:
        keyboard.press('t')
    speak("Done sir")

def ChromeAuto():
    speak("Chrome Automation!!")
    comm = takeCommand()

    if "close this tab" in comm:
        keyboard.press_and_release('ctrl + w')

    elif 'open this tab' in comm:
        keyboard.press_and_release('ctrl + t')

    elif 'open new window' in comm:
        keyboard.press_and_release('ctrl + n')

    elif 'history' in comm:
        keyboard.press_and_release('ctrl + h ')

def Dict():
    speak("Opening dictionary!")
    speak("Tell me the word for search!!")
    word = takeCommand()

    if 'meaning' in word:
        word = word.replace("what is the", "")
        word = word.replace("friday","")
        word = word.replace("of", "")
        word = word.replace("meaning", "")
        result = Dictionary.meaning(word)
        speak(f"The Meaning for {word} is {result}")

    elif 'synonym' in word:
        word = word.replace("what is the", "")
        word = word.replace("friday","")
        word = word.replace("of", "")
        word = word.replace("synonym", "")
        result = Dictionary.synonym(word)
        speak(f"The Synonym for {word} is {result}")


    elif 'antonym' in word:
        word = word.replace("what is the", "")
        word = word.replace("friday","")
        word = word.replace("of", "")
        word = word.replace("antonym", "")
        result = Dictionary.antonym(word)
        speak(f"The Antonym for {word} is {result}")
    speak("Dictionary ended sir!!")

def TakeScreenShot():
    speak("Ok Boss,What Should I call it??")
    path = takeCommand()
    imgPath = path + ".png"
    path1 = "C:\\Users\\Universe\\Pictures\\Screenshots" + imgPath
    sc = pyautogui.screenshot()
    sc.save(path1)
    os.startfile("C:\\Users\\Universe\\Pictures")
    speak("Here is the snapshot captured!!")

def Temp():
    search = "temperature in kakinada"
    url = "https://www.google.com/search?q=" + search
    j = requests.get(url)
    data = BeautifulSoup(j.text,"html.parser")
    temperature = data.find("div",class_="BNeawe").text
    speak(f"The Temperature in kakinada is {temperature} outside")

def Reader():
    speak("Reading your book Sir!!")
    os.startfile("D:\\book\\Ethfrog.pdf")
    book = open("D:\\book\\Ethfrog.pdf",'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.getNumPages()
    speak(f'Number of pages in this book are {pages}')
    speak(f'From which page I have To start Reading??')
    numPage = int(input())
    page = pdfReader.getPage(numPage)
    text = page.extractText()
    speak("Choose the language Sir!!")
    lang = takeCommand()

    if 'hindi' in lang.lower():
        trans1 = Translator()
        textHin = trans1.translate(text,'hi')
        textfile=textHin.text
        speech = gTTS(text=textfile)
        try:
            speech.save('book.mp3')
            playsound('book.mp3')
        except:
            playsound('book.mp3')
    else:
        speak(text)

def SpeedTest():
    import speedtest
    speak("checking speed....")
    playsound("Jarvis On.mp3")
    speed = speedtest.Speedtest()
    downloading = speed.download()
    correctDown = int(downloading/800000)
    uploading = speed.upload()
    correctUpload = int(uploading/800000)

    if 'uploading' in query:
        speak(f'The uploading Speed is {correctUpload} mbps')
    elif 'downloading' in query:
        speak(f'The downloading speed is {correctDown} mbps')
    else:
        speak(f'The Downloading speed is {correctDown} and the uploading speed is {correctUpload}')

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak(f'Searching for{query}....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'hi friday' in query:
            speak("Hi Boss!!. I am friday")
            speak("How may I assist you?")

        elif "hello friday" in query:
            speak("Hello Boss!!. I am friday")
            speak("What can I do for you")

        elif "how are you" in query:
            speak("I am 1s and 0s")
            speak("whats about you boss?")

        elif "you need a break" in query:
            speak("ok boss, You can call me Anytime!")
            speak("Just say wake up Friday!!")
            break

        elif 'youtube search' in query:
            speak("Ok boss,I found this on youtube")
            query = query.replace("friday", "")
            query = query.replace("youtube search", "")
            ytUrl = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(ytUrl)
            speak("Done Boss")

        elif "website" in query:
            speak("Ok boss,Launching your request...")
            query = query.replace("friday", "")
            query = query.replace("website", "")
            web1 = query.replace("open", "")
            webUrl = "https://www." + web1 + ".com"
            webbrowser.open(query)
            speak("Done Boss")

        elif 'open google' in query:
            OpenApps()

        elif 'open youtube' in query:
            OpenApps()

        elif 'open facebook' in query:
            OpenApps()

        elif 'open github' in query:
            OpenApps()

        elif 'open code' in query:
            OpenApps()

        elif 'open word' in query:
            OpenApps()

        elif 'open speed' in query:
            OpenApps()

        elif 'open chrome' in query:
            OpenApps()

        elif 'open spotify' in query:
            OpenApps()

        elif 'close chrome' in query:
            CloseApp()

        elif 'stop music' in query:
            CloseApp()

        elif 'play music' in query:
            music_dir = 'E:\\Music\\songs'
            songs = os.listdir(music_dir)
            num = random.randint(0, len(songs))
            speak("Playing Music!!")
            os.startfile(os.path.join(music_dir, songs[num]))
            speak("Done Boss")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")
            speak("Done Boss")

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

        elif 'whatsapp' in query:
            Whatsapp()

        elif "kill" in query:
            speak("killing friday")
            exit()

        elif 'pause' in query:
            keyboard.press("space bar")

        elif 'restart' in query:
            keyboard.press("0")

        elif 'mute' in query:
            keyboard.press("m")

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'Theater mode' in query:
            keyboard.press('t')

        elif 'youtube auto' in query:
            YoutubeAuto()

        if "close this tab" in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open this tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in query:
            keyboard.press_and_release('ctrl + h ')

        elif 'chrome auto' in query:
            ChromeAuto()

        elif 'repeat my words' in query:
            speak("ok sir!!, Speak Now")
            words = takeCommand()
            speak(f"You Said: {words}")

        elif 'my location' in query:
            speak("ok Sir, Wait a second")
            locUrl = "https://www.google.co.in/maps/place/16%C2%B058'09.5%22N+82%C2%B013'57.8%22E/@16.9692233,82.2324985,16z/data=!4m6!3m5!1s0x3a382813be53ed65:0x5e9b46b0ea8af152!7e2!8m2!3d16.9692931!4d82.2327089?hl=en&authuser=0"
            webbrowser.open(locUrl)

        elif 'dictionary' in query:
            Dict()

        elif 'screenshot' in query:
            TakeScreenShot()

        elif 'alarm' in query:
            speak("Enter the Time!")
            time = input(":Enter the Time:")
            while True:
                time_at = datetime.datetime.now()
                now = time_at.strftime("%H:%M:%S")
                if now == time:
                    speak("Time to wake up Sir!!")
                    playsound("alarm.mp3")
                speak("Alarm has been Started")

        elif "online jarvis" in query:
            playsound("jarvisIntro.mp3")
            friday.setProperty('voice', voices[0].id)

        elif "online friday" in query:
            friday.setProperty('voice', voices[3].id)
            speak("I am friday. Your Personal Assistant. Lets rock and roll")
            speak("What can I do For you")

        elif 'video downloader' in query:
            speak("Opening Video Downloader")
            root = Tk()
            root.geometry('500x300')
            root.resizable(0, 0)
            root.title("Youtube Video Downloader")
            speak("Enter the Youtube link here!!")
            Label(root, text="Youtube Video Downloader", font="arial 15 bold").pack()
            link = StringVar()
            Label(root, text="Place Your Youtube URL Link", font="arial 15 bold").place(x=80, y=60)
            Entry(root, width=70, textvariable=link).place(x=32, y=90)


            def VideoDownloader():
                url = YouTube(str(link.get()))
                video = url.streams.first()
                video.download()
                Label(root, text="Download", font="arial 15").place(x=180, y=210)


            Button(root, text="Download", font="arial 15 bold", bg="pale violet red", padx=2,
                   command=VideoDownloader).place(x=180, y=150)

            root.mainloop()
            speak("Video Downloaded")

        elif "translate in telugu" in query:
            Trans()

        elif "remember that" in query:
            rememberMsg = query.replace("remember that","")
            rememberMsg = query.replace("friday","")
            speak("Tell me What to remind you :"+ rememberMsg)
            remember = open("data.txt",'w')
            remember.write(rememberMsg)
            remember.close()

        elif 'what do you remember' in query:
            remind = open('data.txt','r')
            speak("I remember that Sir to remind you:" + remind.read())


        elif 'google search' in query:
            import wikipedia as googleScarp
            query = query.replace("friday","")
            query = query.replace("google search","")
            query=query.replace("google","")
            speak("This is What I found for your search")

            try:
                pywhatkit.search(query)
                result = googleScarp.summary(query,3)
                speak(result)

            except:
                speak("No data found")

        elif 'temperature' in query:
            Temp()

        elif 'download speed' in query:
            SpeedTest()

        elif 'upload speed' in query:
            SpeedTest()

        elif 'internet speed' in query:
            SpeedTest()

        elif 'how to' in query:
            speak("Getting data From cloud!!")
            op = query.replace("friday","")
            max_result = 1
            how_to_func = search_wikihow(op,max_result)
            assert len(how_to_func)==1
            how_to_func[0].print()
            speak(how_to_func[0].summary)

        elif 'read book' in query:
            speak("Your book is eat that frog")
            Reader()

        elif 'whatsapp message' in query:
            speak("To whom should I send??")
            name = takeCommand()

            if 'Amma' in name:
                num = "*************"
                speak(f"Should I ping {name}??")
                mess = takeCommand()
                speak("specify time in hr")
                hr = takeCommand()
                speak("specify time in min")
                min = takeCommand()
                whatsapp.whatsapp(num, mess, hr, min)
                speak("Message sent successfully")


            elif 'Akka' in name:
                num = "************"
                speak(f"Should I ping {name}??")
                mess = takeCommand()
                speak("specify time in hr")
                hr = takeCommand()
                speak("specify time in min")
                min = takeCommand()
                whatsapp.whatsapp(num, mess, hr, min)
                speak("Message sent successfully")


            elif 'family' in name:
                gro = "**********"
                speak(f'What shall I send to group {gro}')
                mess = takeCommand()
                speak("specify time in hr")
                hr = takeCommand()
                speak("specify time in min")
                min = takeCommand()
                whatsapp.Whatsapp_Grp(gro, mess, hr, min)
                speak("Message sent successfully")

        elif "message now" in query:
            speak("To whom should I send??")
            name = takeCommand()

            if 'Name1' in name:
                num = "***********"
                mess = takeCommand()
                whatsapp.WhatsAppInstant(num, mess)
                speak("Message sent successfully")


            elif 'Name2' in name:
                num = "********"
                speak(f"Should I dm {name}??")
                mess = takeCommand()
                whatsapp.WhatsAppInstant(num, mess)
                speak("Message sent successfully")