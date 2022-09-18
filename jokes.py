import pyjokes
import pyttsx3

def Joke():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()
    
    my_joke = pyjokes.get_joke(language='en', category='all')
    print(my_joke)
    speak(my_joke)