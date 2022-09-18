def RandomAdvice():
    import requests
    import pyttsx3

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    url = 'https://api.adviceslip.com/advice'

    def RandAdv():
        data = requests.get(url)
        json_data = data.json()
        random_advice = json_data["slip"]
        print(random_advice["advice"])
        speak(random_advice["advice"])

    RandAdv()