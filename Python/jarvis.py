#install pyaudio "pip install pyaudio"

import requests
from pprint import pprint
import pyttsx3 #install pyttx3 "pip install pyttsx3"
import speech_recognition as sr  #pip install  speechrecognition
import datetime 
import wikipedia #install wikipedia "pip install wikipedia"
import webbrowser
import os
import smtplib
from googlesearch import search #pip install googlesearch
from omdbapi.movie_search import GetMovie #pip install omdb
from datetime import date

engine = pyttsx3.init('sapi5')
voices: object = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=1 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am jarvis. Please tell me how may I help you")

def takeCommand():

    with sr.Microphone() as source:
     r = sr.Recognizer()
      
     print("Please wait. Calibrating microphone...")  
       
     r.adjust_for_ambient_noise(source, duration=10)  
     print("Say something!")
     speak("say something!")
       
     audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception:
        
        speak("Say that again please...")
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Enter your email ID', 'Enter Pass') #enter email ID and pass
    server.sendmail('Enter your email ID', to, content)#enter email ID
    server.close()


def temp():
    
    speak('Enter your city : ')
    city = s_input()

    print(f"User said city name is : {city}\n")
    
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid= "enter ApI key" &units=metric'.format(city) #from openweatherreport

    res = requests.get(url)
    data = res.json()
    temp = data['main']['temp']
    wind_speed = data['wind']['speed']

    latitude = data['coord']['lat']
    longitude = data['coord']['lon']

    description = data['weather'][0]['description']

    speak('Temperature : {} degree celcius'.format(temp))
    speak('Wind Speed : {} m/s'.format(wind_speed))
    speak('Latitude : {}'.format(latitude))
    speak('Longitude : {}'.format(longitude))
    speak('Description : {}'.format(description))

    print('Temperature : {} degree celcius'.format(temp))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('Latitude : {}'.format(latitude))
    print('Longitude : {}'.format(longitude))
    print('Description : {}'.format(description))

def google():
   
         query = s_input()
         for j in search(query, tld="co.in,.com.org.in", num=10, stop=1, pause=2): 
	         print(j) 

def s_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:  
     print("Please wait. Calibrating microphone...")  
       
     r.adjust_for_ambient_noise(source, duration=5)  
     print("Giv input for function")
     speak("Giv input for function")
       
     audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"you said: {query}\n")

    except Exception:
        
        speak("Say that again please...")
        return "None" 
    return query       
def omdb():

    speak('enter name of movie:')
    name = s_input()
    
    movie = GetMovie(title=name, api_key='Enter API key ') #get api key from imdb
    print (movie.get_data('Title'))
    print (movie.get_data('Yaer'))
    print (movie.get_data('Rated'))
    print (movie.get_data('Language'))
    print (movie.get_data('Director'))
    print (movie.get_data('Actors'))
    print (movie.get_data('writer'))
    print (movie.get_data('Ratings'))
    print (movie.get_data('Runtime'))
    print (movie.get_data('Boxoffice'))
    print (movie.get_data('Genre'))
    print (movie.get_data('imdbRating'))

    speak (movie.get_data('Title'))
    speak (movie.get_data('Yaer'))
    speak (movie.get_data('Language'))
    speak (movie.get_data('Director'))
    speak (movie.get_data('Actors'))
    speak (movie.get_data('writer'))
    speak (movie.get_data('Runtime'))
    speak (movie.get_data('Genre'))
    speak (movie.get_data('imdbRating'))



if __name__ == "__main__":

    wishMe()
    while True:

        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "google")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'google' in query:
            speak("opening google")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("opening stackoverflow ")
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'set path to the song' # like F:\\music
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'the date' in query:
        
            today = date.today()
            # dd/mm/YY
            d1 = today.strftime("%d/%m/%Y") 
            speak(f"sir, the date is", d1) 

        elif 'open code' in query:
            codePath = "C:\\Users\\my world\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe" #set path to the vc code exe file
            os.startfile(codePath)

        elif 'open D Drive' in query:
            drivePath = 'H:\\'
            os.startfile(drivePath)
                  

        elif 'email to ' in query:
            try:
                speak("What should I say?")
                content = s_input()
                to = "Enter email for send" #enter email id 
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend dev bhai. I am not able to send this email")
        elif 'weather report' in query:
         content = temp()  

        elif 'search on google' in query:
         content = google()

        elif 'movie detail' in query:
         content= omdb()

        elif 'stop' in query:
            os._exit()
           

          