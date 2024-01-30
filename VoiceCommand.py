import speech_recognition as sr

recognizer = sr.Recognizer()

def talk():
    mic = sr.Microphone()
    with mic as source:

        audio = recognizer.listen(source)
        print(audio)
        try:
            text = recognizer.recognize_google(audio, language='ES')
        except:
            text = 'try again'
            print('what did you say?')
        else:
            print(f'you said: {text}')
        return text.lower()