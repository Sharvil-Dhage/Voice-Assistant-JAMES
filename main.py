import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime as dt
import webbrowser
import pyjokes



listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate", 200)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    talk("JAMES Initialising")
    talk("Initialisation Done")

    hour = int(dt.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Morning Sir!")

    elif hour>=12 and hour<18:
        talk("Good Afternoon Sir!")   

    else:
        talk("Good Evening Sir!")  

    talk("I am James! , How may I help you")  

 
 
 
def hear():
    try:
        with sr.Microphone() as source:
            print("Listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command =command.lower()
            if 'james' in command:
                command = command.replace('james','')
                
    except:
        pass    
    return command


greet()

if __name__ == "__main__":
    while True:
        try:
            command = hear()
            if 'play' in command:
                song = command.replace('play','')
                pywhatkit.playonyt(song)
                print("Playing"+song)
                talk("Playing"+song)
            elif 'search' in command:
                search = command.replace('search','')
                talk("Searching"+search)
                print("Searching"+search)
                pywhatkit.search(search)
        
            elif 'mail' in command:
                print("Opening G Mail")
                talk("Opening G mail")
                webbrowser.open("https://mail.google.com/")

            elif 'joke' in command:
                talk("Sure Sir")
                talk(pyjokes.get_joke())    
            elif 'shutdown' in command:
                talk("Shutting Down")
                break    
        except:
            pass        

        