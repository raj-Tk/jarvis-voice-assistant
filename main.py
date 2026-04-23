import os
import eel

from engine.features import *
from engine.command import *

eel.init("www")

# 🔹 Function first
def playAssistantSound():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    music_dir = os.path.join(base_dir, "www", "assets", "vendore", "textillate", "audio", "start_sound_1.mp3")
    
    playsound(music_dir)

# 🔹 Call function
playAssistantSound()

os.system('start msedge.exe --app="http://localhost:8000/index.html"')

eel.start('index.html', mode=None, host='localhost',block=True)


