import pyttsx3
import speech_recognition as sr
import datetime
import os

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
    except sr.RequestError:
        print("Sorry, my speech recognition is down.")
def get_time():
        now =datetime.datetime.now()
        hour =now.strftime( "%I")
        minute= now.strftime("%M")
        am_pm=now.strftime("%p")
        speak (f"the time is {hour}:{minute}:{am_pm}")
def get_name():
            speak ("My name is Tasnim")
def create_note():
            speak("what should i wrote in the note")
            note_text=listen()
            filename=datetime.datetime.now().strftime("%Y.%m.%d_%S")+".text"
            with open(filename ,"w") as f:
                f.write(note_text)
                f.write(note_text)
            speak("note saved")
def main():
      speak("hi ! how can i help you ?")
      while True :
            command =listen()
            if "hello" in command :
                  speak("Hi")
            elif "how are you?" in command:
                  speak("fine and you")
            elif "what's your name" in command:
                  get_name()
            elif "time" in command:
                  get_time()
            elif "note" in command:
                  create_note()
            elif "goodbye" in command:
                  speak ("goodbye")
            elif 'exit' in command:
                 speak("Thanks for giving me your time")
                 exit()
            elif "who made you" in command or "who created you" in command: 
                   speak("I have been created by Tasnim.")
            else :
                  speak("sorry i can't undersatnd")
                  