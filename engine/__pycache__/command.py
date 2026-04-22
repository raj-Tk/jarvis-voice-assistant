import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init()

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 180)
    print(voices)
    engine.say(text)
    engine.runAndWait()

def takecommand():

    r =sr.Recognizer()

    with sr.Microphone() as source:
        print('listening...')
        r.pause_thresold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, 10, 6) # 10sec for the pause and 6 sec take the speech of the user
    
    try:
        print('recogninition')
        query = r.recognize_google(audio, language='end-in')
        print(f"user said: {query}")

    except Exception as e:
        return ""
    
    return query.lower()

text = takecommand()

speak(text)
