from playsound import playsound 
import eel

#playing assistant sound function 
@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\vendore\\textillate\\audio\\start_sound.mp3"
    playsound(music_dir)