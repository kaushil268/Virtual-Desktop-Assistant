import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am SIRI . how may I help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kaushil268@gmail.com', 'password')
    server.sendmail('kaushil268@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.co.in/")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")


        elif 'play old town road' in query:
            webbrowser.open("https://www.youtube.com/watch?v=r7qovpFAGrQ")


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open word' in query:
            word = "C:\\Users\\Kaushil\\Desktop\\Word"
            os.startfile(word)

        elif 'open powerpoint' in query:
            powerpoint = "C:\\Users\\Kaushil\\Desktop\\PowerPoint"
            os.startfile(powerpoint)

        elif 'open spotify' in query:
            spotify = "C:\\Users\\Kaushil\\Desktop\\Spotify"
            os.startfile(spotify)

        elif 'open this pc' in query:
            thispc = "C:\\Users\\Kaushil\\Desktop\\This PC"
            os.startfile(thispc)

        elif 'open discord' in query:
            discord = "C:\\Users\\Kaushil\\Desktop\\Discord"
            os.startfile(discord)

        elif 'open word' in query:
            gameloop = "C:\\Users\\Kaushil\\Desktop\\Gameloop"
            os.startfile(gameloop)





