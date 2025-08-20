import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
import google.generativeai as genai
import time


news_api = "200a7285198a4f018607e76259e648c7"
recognizer = sr.Recognizer()
sound = pyttsx3.init()
def speak(text):
    sound.say(text)
    sound.runAndWait()

def aiprocess(command):
    
    genai.configure(api_key="AIzaSyCqjd0KE18CQRf9qRs3Hqj5SkyS7q9Tk-A")

    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(command)
    return response.text


def processcommand(c):
    c = c.lower()
    if("open google" in c):
        speak("opening google")
        webbrowser.open("https://www.google.com")
        
    elif("open youtube" in c):
        speak("opening youtube")
        webbrowser.open("https://www.youtube.com")
        
    elif("open facebook" in c):
        speak("opening facebook")
        webbrowser.open("https://www.facebook.com")
        
    elif("open linkedin" in c or "linked in" in c):
        speak("opening linkedin")
        webbrowser.open("https://in.linkedin.com")
        
    elif("open chatgpt" in c or "chat gpt" in c):
        speak("opening chatgpt")
        webbrowser.open("https://chatgpt.com")
        
    elif c.lower().startswith("play"):
        speak("playing")
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
        
    elif "today's news" in c or "news" in c:
        speak("Fetching today’s headlines, please wait.")
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=200a7285198a4f018607e76259e648c7")

        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])

            if not articles:
                speak("Sorry, I could not find any news right now.")
            else:
                speak("Here are the top 5 headlines.")
                for article in articles[:5]:   # limit to 5
                    title = article.get("title", "No title")
                    speak(title)
                    
                   # print("Headline:", title)  # for debugging

        else:
            print("Error:", r.status_code, r.text)  # debug info
            speak("Sorry, I could not fetch the news.")

    elif("stop" in c.lower()):
        speak("Terminating...")
        exit()


# let openai handle the requests
    else:
        output = aiprocess(c)
        speak(output)
        


if __name__== "__main__":
    speak("Initializing Jarvis.....")
    
    # Wake up only once
    while True:
        try:
            with sr.Microphone() as source:
                print("Say 'Jarvis' to wake me up...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            word = recognizer.recognize_google(audio)
            print(word)

            if word.lower() == "jarvis":
                speak("Yes sir, I am listening...")
                break   # Exit wake loop
        except Exception as e:
            print("Error:", e)

    # Now keep listening until stop
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for command...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio)
            print("Command:", command)

            processcommand(command)
        except Exception as e:
            print("Error:", e)