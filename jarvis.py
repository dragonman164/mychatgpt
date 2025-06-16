# pip install SpeechRecognition pyttsx3 wikipedia
# pip install pipwin
# pip install pyaudio

import speech_recognition as sr
import pyttsx3
import wikipedia
import datetime

# Initialize the recognizer and engine
listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source, timeout=5)
            command = listener.recognize_google(voice)
            command = command.lower()
            print("You said:", command)
            if "jarvis" in command:
                command = command.replace("jarvis", "")
    except:
        return ""
    return command

def run_jarvis():
    command = listen_command()

    if "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("Current time is " + time)

    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, sentences=1)
        talk(info)

    elif "what is" in command:
        topic = command.replace("what is", "")
        info = wikipedia.summary(topic, sentences=1)
        talk(info)

    elif "stop" in command or "exit" in command:
        talk("Goodbye!")
        exit()

    else:
        talk("Sorry, I didn't understand. Can you say that again?")

# Loop forever
while True:
    run_jarvis()
