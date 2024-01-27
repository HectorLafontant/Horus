
import flet as ft
import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()

engine = pyttsx3.init()

def talk():
    while True:
        mic = sr.Microphone()
        with mic as source:
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language='ES')
            print(f'Has dicho: {text}')
            return text.lower()
        except sr.UnknownValueError:
            print("No se detectó ninguna entrada de voz. Por favor, intenta de nuevo.")

if 'estudiantes' in talk():
    engine.say('Buenas, te voy a llevar a {text}')
    engine.runAndWait()

