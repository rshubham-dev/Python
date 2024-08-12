import speech_recognition as sr
import webbrowser
import pyttsx3
import requests

recognizer = sr.Recognizer()
newsapi = "0e17826f6a6144348fe8d37b53f3f134"
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')   
print (rate)                       
engine.setProperty('rate', 220)     # setting up new voice rate
volume = engine.getProperty('volume')  
print (volume)                          
engine.setProperty('volume', 1.0)    # setting up volume level  between 0 and 1


def speak(text):
    engine.say(text)
    # engine.save_to_file(text, 'test.mp3') # to save voice to a file
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            for article in articles:
                print(article['title'])
                speak(article['title'])
        else:
            print(f"Failed to fetch data: {r.status_code} - {r.reason}")
    else:
        pass
        # let OpenAI handel the request
    
if __name__ == "__main__":
    speak("Hello Sir, How May I Help You")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()


        # recognize speech using google
        
        print("Recongizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=2)

            word = r.recognize_google(audio)
            print(word)
            if(word.lower() == "hello"):
                speak("Ya")
                # listen for command
                with sr.Microphone() as source:
                    print("Shubham Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))