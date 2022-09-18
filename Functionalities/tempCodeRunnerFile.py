engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#Speaker Function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()