from logging import fatal
import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os
import wikipedia

wikipedia.set_lang("En")

r = sr.Recognizer()

def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice =""
        try:
            voice = r.recognize_google(audio , language="en-En")
        except sr.UnknownValueError:
            speak("i couldn't understand")
        except sr.RequestError:
            speak("There is problem in the system")
        return voice
    


def response(voice):
    if "how are yo" in voice:
        speak("I m fine sirl and you")

    if 'What is your name' in voice:
        speak('Elman')
        
    if "Good Morning" in voice:
        speak("Good Morning sir")

    if "what time is it" in voice:
        speak(datetime.now().strftime("%H:%M:%S"))

    if "Who is" in voice.split():
        voice=voice.split()
        personname=""
        for i in voice[:-1]:
            personname = personname + "" +i
        wiki=wikipedia.summary(personname,sentences=1)  
        url="https://www.google.com/search?q="+personname
        webbrowser.get().open(url)
        speak(wiki)

    if 'Song' in voice:
        speak('opens sir')
        url = 'https://www.youtube.com/watch?v=XuLstZlUdMc&list=PLxdLmh0FDYFc_0JIuyXCy2qSCkt1H-oIw'
        webbrowser.get().open(url)

    if 'Who made you' in voice or 'who is your creator' in voice:
        speak('My creator Cinar sak. To communicate with my creator, here is his site')
        url = 'http://cinarsak.cf'
        webbrowser.get().open(url)


    if "okay" in voice:
        speak("see you sir ")
        exit()


def search(voice):
    if 'search' in voice:
        search = record("What do you want me to search right away sir?")
        url = 'https://www.google.com/search?q='+search
        webbrowser.get().open(url)
        speak(search + "Result for")


    if 'weather status' in voice or 'what is the air temperature' in voice or 'what is temperature' in voice:
        speak('Opens')
        url = 'https://www.google.com/search?q=hava+durumu&oq=hava&aqs=chrome.0.69i59l2j69i57j0l5.2820j1j9&sourceid=chrome&ie=UTF-8'
        webbrowser.get().open(url)

    if 'YouTube' in voice:
        search = record("what would you like to watch sir ")
        url = 'https://www.youtube.com/results?search_query='+search
        webbrowser.get().open(url)
        speak(search + "Results for")

        
def locations(voice):
    if "Where" in voice.split():
        voice=voice.split()
        location=""
        for i in voice[:-1]:
            location = location + "" +i
        url="https://www.google.com/maps/place/"+location
        webbrowser.get().open(url)
    

def speak(string):
    tts = gTTS(string,lang="en",slow=False)
    rand = random.randint(1,10000)
    file = "audio-"+str(rand)+".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)


def internet(voice):
    if 'news' in voice:
        speak('opened sir')
        url = 'https://globalnews.ca'
        webbrowser.get().open(url)

    if 'what is it agenda' in voice:
        speak('agenda is opened sir')
        url = 'https://globalnews.ca/?s=agenda'
        webbrowser.get().open(url)

    if 'Sport news' in voice:
        speak('Sport news is opened sir ')
        url = 'https://www.haberturk.com/spor'
        webbrowser.get().open(url)
    
    if "I'm hungry" in voice:
        search = record('what would you like to eat sir ')
        url = 'https://www.yemeksepeti.com/your-city/arama#ors:true|st:' + search
        webbrowser.get().open(url)
        speak(search + 'Results for')

    if 'Twitter' in voice:
        speak("Twitter is opened ")
        url = 'https://twitter.com/i/trends'
        webbrowser.get().open(url)

    if 'foreign currency' in voice:
        speak("exchange opened sir")
        url = 'https://www.doviz.com'
        webbrowser.get().open(url)


    if 'world news' in voice:
        speak('world news opens')
        url = 'https://www.haberturk.com/dunya'
        webbrowser.get().open(url)


    if 'action movies' in voice:
        speak('action movies opens sir')
        url = 'https://www.fullhdfilmizlesene.com/filmizle/aksiyon-hd-film-izle'
        webbrowser.get().open(url)

    if 'science fiction movies' in voice:
        speak('science fiction movies opens sir ')
        url = 'https://www.fullhdfilmizlesene.com/filmizle/bilim-kurgu-filmi-izle'
        webbrowser.get().open(url)

    if 'Fantastic movies' in voice:
        speak('fantastic movies opens sir')
        url = 'https://www.fullhdfilmizlesene.com/filmizle/fantastik-film-izle'
        webbrowser.get().open(url)
        
    if 'Animation movies' in voice:
        speak('animation movies opens sir')
        url = 'https://www.fullhdfilmizlesene.com/filmizle/animasyon-film-izle'
        webbrowser.get().open(url)

    if 'Comedy movies' in voice:
        speak('Comedy movies opens sir') 
        url = 'https://www.fullhdfilmizlesene.com/filmizle/komedi-film-izle'
        webbrowser.get().open(url)

    if 'War movies' in voice:
        speak('War movies opens sir')
        url = 'https://www.fullhdfilmizlesene.com/filmizle/savas-filmleri-izle'
        webbrowser.get().open(url)

    if 'Horror movies' in voice:
        speak('horror movies opens sir')
        url = 'https://www.fullhdfilmizlesene.com/filmizle/korku-film-izle'
        webbrowser.get().open(url)

    if 'Advanture movies' in voice:
        speak('advanture movies opens sir')
        url = 'https://www.fullhdfilmizlesene.com/filmizle/macera-film-izle'
        webbrowser.get().open(url)

    if 'History movies' in voice:
        speak('History movies opens')
        url = 'https://www.fullhdfilmizlesene.com/filmizle/tarih-film-izle'
        webbrowser.get().open(url)

    if 'romantic movies' in voice:
        speak('romantic movies opens')
        url = 'https://www.fullhdfilmizlesene.com/filmizle/romantik-filmler-izle'
        webbrowser.get().open(url)

    if 'Dramam movies' in voice:
        speak('drama movies opens sir')
        url = 'https://www.fullhdfilmizlesene.com/filmizle/dram-film-izle'
        webbrowser.get().open(url)
    

        



speak("sir how can i help you")
time.sleep(1)

while 1:
    voice=record()
    print(voice)
    response(voice) 
    search(voice)
    locations(voice)
    internet(voice)