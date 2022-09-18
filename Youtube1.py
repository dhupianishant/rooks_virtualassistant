def SongName():
    import pyttsx3
    import speech_recognition as sr
    import datetime
    import wikipedia
    import os
    import smtplib
    import sys
    import webbrowser
    import cv2
    import requests
    import pywhatkit


    engine = pyttsx3.init('sapi5')

    # Set Rate
    engine.setProperty('rate', 190)

    # Set Volume
    engine.setProperty('volume', 1.0)

    # Set Voice (Female)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)


    def speak(text):
        """Used to speak whatever text is passed to it"""

        engine.say(text)
        engine.runAndWait()

    def take_user_input():
        """Takes user input, recognizes it using Speech Recognition module and converts it into text"""
        
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening....')
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-in')
            if not 'exit' in query or 'stop' in query:
                speak(choice(opening_text))
            else:
                hour = datetime.now().hour
                if hour >= 21 and hour < 6:
                    speak("Good night sir, take care!")
                else:
                    speak('Have a good day sir!')
                exit()
        except Exception:
            speak('Sorry, I could not understand. Could you please say that again?')
        return query




    def YouTubeSearch(term):
        result = "https://www.youtube.com/results?search_query=" + query

        webbrowser.open(result)

        speak("This is what i have found for you")

        pywhatkit.playonyt(term)

        speak("This may also help you sir .")


    query = take_user_input().lower()
    
