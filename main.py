import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os

print("************WEDNESDAY AI**************")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


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

    speak("I am Wednesday Sir. Please tell me how may I help you")       

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
        speak("Sorry i could not recognize it plz say that again sir...")  
        return "None"
    return query

if __name__ == "__main__": 
    print("I am Wednesday Sir. Please tell me how may I help you")
    wishMe()
    while True:
        query = takeCommand().lower()

        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],["chatgpt","https://chat.openai.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speak(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        if "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            speak(f"Sir time is {hour} and {min} minutes")

        elif "open music" in query:
            os.startfile(r"C:/Users/Omkar/Downloads/Cheques_320(PagalWorld.com.pe).mp3")

        elif "open whatsapp".lower() in query.lower():
            os.startfile("C:/Users/Omkar/Desktop/WhatsApp.lnk")

        elif "open chrome".lower() in query.lower():
            os.startfile("C:/Users/Public/Desktop/Google Chrome.lnk")
        
        elif "quit".lower() in query.lower():
            exit()
