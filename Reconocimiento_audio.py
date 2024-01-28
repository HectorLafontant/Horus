
import flet as ft
import speech_recognition as sr #Libreria para utilizar el microfono y reconocer voz
import pyttsx3 #Libreria para que hable la maquina

recognizer = sr.Recognizer() #Para que reconozca la voz y la guardamos en una variable

engine = pyttsx3.init() #Para que la maquina nos pueda hablar

def talk(): #Función donde se realizaran las condiciones para el reconocimiento
    mic = sr.Microphone() #Se utiliza para que se reconozca el microfono, es necesario tenerlo activo
    with mic as source: #Que detecte todo lo que decimos
        audio = recognizer.listen(source) #Nueva variable para que nos escuche 

        text = recognizer.recognize_google(audio, language='ES') #Funcion para que nos comprenda en español lo que tenemos guardado en la varibale audio 
        print(f'Has dicho: {text}') #Que nos escriba por pantalla lo que dijimos
        return text.lower() #Para que lo devuelva en minuscula
    
if 'estudiantes' in talk(): #Si nosotros decimos algo especificado, en este caso estudiante hago lo siguiente
    engine.say('Buenas, te voy a llevar a listas de estudiantes') #Nos va a decir la maquin lo que este escrito aqui
    engine.runAndWait() #para que ejecute y espere

