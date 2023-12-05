import speech_recognition as sr

def speechtotext():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            voice_data = ""
            voice_data = r.recognize_google(audio)
            return voice_data
        except sr.UnknownValueError:
            print("error")
        except sr.RequestError:
            print("Request Error")