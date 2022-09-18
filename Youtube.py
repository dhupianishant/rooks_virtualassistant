def YouTubeSearch():
    import pyttsx3
    import pywhatkit
    import speech_recognition as sr 
    
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()
    
    def TakeSong():
        r = sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source) #reduce noise
            r.pause_threshold = 0.5
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query1 = r.recognize_google(audio, language='en-in')
            print(f"User said: {query1}\n")

        except Exception as e:
            # print(e)    
            print("I was not able to process that, can you please repeat it...")  
            return "None"
        return query1    

    TakeSong()
    
    result = "https://www.youtube.com/results?search_query=" + query1
    web.open(result)
    speak("This is what i have found for you")
    pywhatkit.playonyt(term)
    speak("This may also help you sir .")

YouTubeSearch()    
