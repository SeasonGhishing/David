import pyttsx3
import speech_recognition as rs


#  pyttsx3 is a text to speech converter python inbuilt module.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[2].id) # prints the voiceover's name
engine.setProperty('voice', voices[0].id)

'''say function is for the voice assistant to speak the programmed things.'''
def say(audio):
    engine.say(audio)
    engine.runAndWait()


'''command function is for taking the voice of the user form device microphone in the form of string. '''
def command():
    # takes input from microphone and returns string output.
    r = rs.Recognizer()
    with rs.Microphone() as source:
        print("I am listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        # r.energy_threshold = 200
        audio = r.listen(source)
        
    try:
        print("Recognizing...\n")
        user_audio = r.recognize_google(audio, language='en-in')
        print(f"User said: {user_audio}\n")
    except Exception as e:
        say("Didn't get it. Say again...")
        return "None"
    return user_audio