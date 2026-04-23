import os
import re

from playsound import playsound 
import eel
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit

#playing assistant sound function 
@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\vendore\\textillate\\audio\\start_sound.mp3"
    playsound(music_dir)



def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open","")
    query =query.lower()

    if query!="":
        speak("Opening"+query)
        os.system('start ' +query)
    else:
        speak("not found")

def PlayYoutube(query):
    search_term = extract_yt_term(query)

    if not search_term:
        speak("I could not find what to play on YouTube")
        return

    speak("Playing "+search_term+" on YouTube")

    kit.playonyt(search_term)

def extract_yt_term(command):
    command = command.lower()
    if "on youtube" in command:
        pattern = r'play\s+(.*?)\s+on\s+youtube'
    else:
        pattern = r'play\s+(.*)' #define dynamic term (.*?) mostly song name it is get extrated 
    
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None