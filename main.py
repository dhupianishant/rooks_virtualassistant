#Importing Modules
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import smtplib
import sys
import webbrowser
import cv2
import pyjokes
import geocoder
import requests
import time
import pywhatkit

#Initialising Camera
cam = cv2.VideoCapture(0)
from mediapipe import solutions as sol

#Initialising Speaker Voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#Speaker Function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

    
#Greeting Function
def wishMe():
    '''hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")'''  

    speak("Hello, My name is Rooks. How may I help you")       

#Take Voice Input
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source) #reduce noise
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("I was not able to process that, can you please repeat it...")  
        return "None"
    return query

#Send Mails
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youemail', 'password')
    server.sendmail('othersemail', to, content)
    server.close()

#Main Program
if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        #Wikipedia
        if 'wikipedia' in query:
            from wikipedia import Wikipedia
            Wikipedia()

        #YouTube
        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        #Google
        elif 'google' in query:
            webbrowser.open("www.google.com")
        
        #WhatsApp
        elif 'whatsapp web' in query:
            webbrowser.open("https://web.whatsapp.com")
        
        #StackOverflow
        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
        
        #Spotify
        elif 'spotify' in query:
            webbrowser.open('https://www.spotify.com')    
         
        #Time
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")
           
        #VA Introduction
        elif 'who are you' in query :    
            speak(f"Hello, my name is Rooks. I am a virtual assistant developed by Rookie Coders")
            
        #Reapet after me
        elif 'repeat after me' in query:
            speak(f"What shoul I repeat?")  
            content = takeCommand()
            speak(f"{content}")  
        
        #Personal Intro
        elif 'who am i' in query:
            speak(f"You are Rookie Coders, you are the one who developed me.")
        
        #Google search
        elif 'look for' in query:
            speak('What shoul I surf the net for?')
            content = takeCommand()
            webbrowser.open("{content}")   
        
        #Ends the Program
        elif 'leave' in query:
            speak(f"Thankyou for using me. This is ROOKS signing off.")
            break;
        
        #Hand Gestures
        elif 'camera' in query:
            from hand_gestures import Camera
            Camera()

        #Joke
        elif 'joke' in query:
            from jokes import Joke
            Joke()
        
        #Weather
        elif 'weather' in query:
            from location_weather import Weather
            Weather()
            time.sleep(10)

        #Face Gestures
        elif 'face' in query:
            from facerecognition import Recognize
            Recognize()
        
        #Games
        elif 'mini' in query:
            from tictactoe import TicTacToe
            TicTacToe()
            time.sleep(5)
        
        #Open Notepad
        elif 'notepad' in query:
            codepath = 'C:\\Windows\\notepad.exe'
            os.system(codepath)
        
        #Open Calculator
        elif 'calculator' in query:
            codepath = 'C:\\Windows\\System32\\calc.exe'
            os.system(codepath)
        
        #Give Random Advice
        elif 'advice' in query:
            from advice import RandomAdvice
            RandomAdvice()


        #Song from YoutTube
        elif 'play song' in query:
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
            YouTubeSearch(query)
    
            

