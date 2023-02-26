from David import greet,command,say,now_time
from print import Hello_World_Java, Hello_World_Python
from rm import reading_mode
import wikipedia
# from gtvoice import 
from jokes import tellajoke
from typingmode import typeMode

# inp = command(input("Enter a text")).lower()

if __name__ == "__main__":
    while True:
        query = command().lower()
        if query=="activate command mode":
            cm = say("command mode activated")
            greet()
        
        elif "joke" in query or "jokes" in query:
            tellajoke()
        
        elif "listening" in query:
            say("I am active and listening.") 
             
        elif 'time' in query:
            now_time()
        
        elif query=='shutdown' or query == 'shut down':
            say("""Okay..... 
                3.
                2.
                1.
                I am shuttinng down. goodbye""")
            exit()
        elif "full name" in query:
            say("""Well i really don't have a full name
                But you can call me david johnson..""")
            
        elif 'wikipedia' in query:
            print("fetching...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            say("According to wikipedia...")
            print(results)
            say(results)
            
            
        elif query == "enable typing mode":
            typeMode() 
        elif query =="enable reading mode":
            reading_mode()
        elif query=="print hello world in java":
            Hello_World_Java()
        elif query=="print hello world in python":
            Hello_World_Python()
        else: 
            say("waiting for your command")