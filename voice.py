import pyttsx3
import speech_recognition as sr
import datetime
import os
import requests

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("I am listening")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't understand what you said.")
        return ""
    except sr.RequestError:
        print("Sorry, my speech recognition is down.")
        return ""

def get_time():
    now = datetime.datetime.now()
    formatted_time = now.strftime("%I:%M %p")
    speak(f"The time is {formatted_time}")

def get_name():
    speak("My name is Tasnim")

def create_note():
    speak("What should I write in the note?")
    note_text = listen()
    filename = datetime.datetime.now().strftime("%Y.%m.%d_%S") + ".txt"
    with open(filename, "w") as f:
        f.write(note_text)
    speak("Note saved")

def get_weather(city):
    print(f"Recognized city: {city}")
    api_key = '4906fb074b72a5b7676e82af647c321e'
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        speak(f"The weather in {city} is {weather_description}. The temperature is {temperature} degrees Celsius.")
    else:
        speak("Sorry, I couldn't retrieve the weather information.")
        print("API Response:", response.text)

def main():
    speak("Hi! How can I help you?")
    while True:
        command = listen()
        if "hello" in command:
            speak("Hi")
        elif "how are you" in command:
            speak("Fine, and you?")
        elif "what's your name" in command:
            get_name()
        elif "time" in command:
            get_time()
        elif "note" in command:
            create_note()
        elif "weather" in command:
            speak("Sure, which city's weather would you like to know?")
            city = listen()
            print(city)
            get_weather(city)
        elif "goodbye" in command or 'exit' in command:
            speak("Goodbye. Thanks for giving me your time.")
            exit()
        elif "who made you" in command or "who created you" in command:
            speak("I have been created by Tasnim.")
        else:
            speak("Sorry, I can't understand.")

if __name__ == "__main__":
    main()

