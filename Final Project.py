import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def welcome():
    hour = int(datetime.datetime.now().hour)    
    if hour>=6 and hour<12:
        speak("A very good morning sir")
    if hour >= 12 and hour < 17:
        speak("Good noon sir")
    if hour >= 17 and hour < 19:
        speak("Good evening sir")
    if hour >= 19 and hour < 24:
        speak("working late night sir! ")
        
    speak("I am here to help you.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

 
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print("you said : {}\n".format(query))  

    except Exception as e: 
        print("Say that again please...")   
        return "None" 
    return query



if __name__ == "__main__":
    welcome()
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
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")


        elif 'open code' in query:
            codePath = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open python' in query:
            codePath = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python38\\python.exe"
            os.startfile(codePath)

        elif 'terminate' in query:
            break
