import datetime
import random as rand
import pyttsx3
import webbrowser
import wikipedia
import speech_recognition as rs

rand = rand.randint(1,5)
#  pyttsx3 is a text to speech converter python inbuilt module.
engine = pyttsx3.init('sapi5') # accessing the sapi5.
voices = engine.getProperty('voices')
# print(voices[2].id) # prints the voiceover's name
engine.setProperty('voice', voices[1].id)

def say(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    # takes input from microphone and returns string output.
    r = rs.Recognizer()
    with rs.Microphone() as source:
        print("I am listening...")
        r.pause_threshold = 1
        r.energy_threshold = 470
        # r.energy_threshold = 200
        audio = r.listen(source)
        
    try:
        print("Recognizing...\n")
        user_audio = r.recognize_google(audio, language='en-in')
        print(f"User said: {user_audio}\n")
        
        # unknown value error works for the speech which is not recognized by the assistant.
    except rs.UnknownValueError:
        say("Didn't get it. Say again...")
        return "None"
    
    # Request error works while you don't have an internet connection.
    except rs.RequestError as e:
        print(("""Connection error...
Please check your internet connection\n"""))
        say("""Connection error...
            Please check your internet connection""")
        exit()
    return user_audio
    
moment1 = "day"
moment2 = "night"


def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        say("Good morning")
    elif hour>=12 and hour<17:
        say("good afternoon!")
    else:
        say("Good evening")  

    if(rand==1):
        say("""sir I am David. How may I help you?
            """)

    elif(rand==2):
        if hour>=0 and hour<18:
            say(f"""Isn't it a great {moment1} sir? Is there any way I can assist you? 
                """)
        else:
            say(f"""Isn't it a great {moment2} sir? Is there any way I can assist you?
                """)
             
    elif(rand==3):
        say(""" 
            Hello sir. 
            I hope you are doing well. 
            How may I help you?
            """)

    elif(rand==4):
        say(""" sir. 
            I am onn.
            Hello sir I am david. 
            How may I help you?
            """)

    elif(rand==5):
        say(f"""Welcome sir. 
            how may i assist you?
            """)
        


        
def now_time():
    hour = int(datetime.datetime.now().hour)
    minutes = int(datetime.datetime.now().minute)
    if hour>=0 and hour<12:
        print(f"its {hour}:{minutes} am right now!\n")
        say(f"its {hour} {minutes} AM right now")
    else:
        print(f"its {hour}:{minutes} pm right now!\n")
        say(f"its {hour} {minutes} PM right now")