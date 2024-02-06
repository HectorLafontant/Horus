import speech_recognition as sr

recognizer = sr.Recognizer()

has_micro = True

def talk():
    global has_micro
    if has_micro == False:
        return

    try:
        mic = sr.Microphone()
    except:
        has_micro = False
        print('no default microphone configured')
        return None

    with mic as source:

        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language='ES')
        except:
            text = 'try again'
            print('what did you say?')
        else:
            print(f'you said: {text}')
        return text.lower()