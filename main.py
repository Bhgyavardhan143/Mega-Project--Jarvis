import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests 

recogniser = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "f029a65cfe034b468c047117cdee316e"

def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
       r = requests.get(f"https://newsapi.org/v2/everything?q=technology&language=en&apiKey={newsapi}")
    
    if r.status_code == 200:
        data = r.json()
        
        # 🐛 DEBUGGING STEP: Print the entire response dictionary
        print("--- API RESPONSE DATA ---")
        print(data)
        print("-------------------------")
        
        articles = data.get('articles', [])

        # 🐛 DEBUGGING STEP: Check if articles is empty
        if not articles:
            speak("I received a successful response, but the articles list is empty.")
            print("DEBUG: The 'articles' list is empty. Check your NewsAPI parameters (country/category).")
            return
            
        for article in articles:
            speak(article['title'])

    else:
        # If the status code is not 200 (e.g., 401, 429)
        speak("I am unable to connect to the news server right now.")
        print(f"DEBUG: API Request Failed. Status Code: {r.status_code}. Full Response Text: {r.text}")
       

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        #Listen for the wake word "Jarvis"
        #Obtain audio from microphone
        r= sr.Recognizer()
       

        print("recognizing...")
        #Recognise speech using google
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("Listening..")
                audio = r.listen(source, timeout=3, phrase_time_limit=2)

            word = r.recognize_google(audio)
            if "jarvis" in word.lower():
                speak("Yes")
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)



        except Exception as e:
            print("Error:",e)