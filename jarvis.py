import webbrowser
import speech_recognition as sr
import os
import pyttsx3
import datetime
import wikipedia
import pywhatkit as wk
import pyaudio



# Initialize text to speech engine
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)
engine.setProperty('rate',200)


# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Function to recognize speech
def listen():
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
    return query.lower()


# Function to greet
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. How may I assist you? sir")


# Main function
def main():
    greet()
    while True:
        query = listen()
        if 'what is' in query:
            speak('Searching Wikipedia...')
            query = query.replace("what is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'who is' in query:
                speak('Searching Wikipedia...')
                query = query.replace("who is", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
        elif 'open google' in query:
            print("now what should i search")
            speak("opening google... now what should i search")
            qry = listen().lower()
            webbrowser.open(f"{qry}")
            results = wikipedia.summary(qry, sentences=1)
            speak(results)
            # Todo: search more about any thing available on ethernet
        elif 'open youtube' in query:
            speak("opening the youtube! now what should i search for you.....")
            #this pywhatkit is specially installed for listen the....
            qry = listen().lower()
            wk.playonyt(f"{qry}")
        elif 'search youtube' in query:
            query = query.replace('search youtube',"")
            print(f"{query}")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        elif 'iron man' in query:
            speak("opening movie ironman sir amaan pasha")
        elif 'the time' in query:
            hor = datetime.datetime.now().strftime("%H")
            mine = datetime.datetime.now().strftime("%M")
            speak(f"The time is{hor} bajhhkke {mine} minutes ho chuke hai")
        elif 'weather' in query:
            speak("so todays weather is as follows: ")
            os.system("start https://www.google.com/search?q=weather+of+today&gs_ivs=1#tts=0")
        elif 'my computer'.lower() in query:
            speak("opening my computer sir ")
            os.system(f"open /This/PC")
        elif 'neetu mam'.lower() in query:
            print("neetu mam is the humber and sweetest person that sir amaan pasha and i have ever meet!")
            speak("neetu mam is the humber and sweetest person that sir amaan pasha and i have ever meet!")

        elif 'who are you' in query:
            print('my name is jarvis!! and i can do whatever my creator programmed me to do')
            speak('my name is jarvis!! and i can do whatever my creator programmed me to do')
        elif 'close browser' in query:
            os.system("taskkill /f /im msedge.exe")
        elif 'close chrome' in query:
            os.system("taskkill /f /im crome.exe")
        elif 'are you there' in query:
            speak("Always available for your assistance sir")
            print("Always available for your assistance sir")
        elif 'your self' in query:
            speak("hello to every one i am jarvis and i could do some of the important task which is given to me")
        elif 'see you later' in query:
            speak("Goodbye! and take care sir amaan pasha")
            break
        else:
            speak("Sorry, I couldn't understand that sir ")


if __name__== "__main__":
    main()