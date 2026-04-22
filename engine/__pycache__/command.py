import pyttsx3
engine = pyttsx3.init()

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 180)
    print(voices)
    engine.say(text)
    engine.runAndWait()


speak("Hello im Jarvis, how can i help you today is there any thing going in the mind of your ?")
