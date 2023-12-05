import webbrowser
import text_to_speech
import speech_to_text
import datetime

def Action(data):
    user_data = data.lower()

    if "what is your name" in user_data:
        text_to_speech.texttospeech("My name is Ittaachee")
        return "My name is Itachi"

    elif "hello" in user_data or "hi" in user_data:
        text_to_speech.texttospeech("Hi Sir How can I assist you?")
        return "Hi Sir How can I assist you?"
    
    elif "shutdown" in user_data:
        text_to_speech.texttospeech("ok sir")
        return "ok sir"

    elif "time" in user_data:
        cur_time = datetime.datetime.now()
        Time = (str)(cur_time) + " Hour :", (str)(cur_time.minute) + "Minute"
        text_to_speech.texttospeech(Time)
        return Time

    elif "youtube" in user_data:
        text_to_speech.texttospeech("Opening Youtube")
        webbrowser.open("https://youtube.com/")
        return "Opening Youtube"

    elif "erp" in user_data:
        text_to_speech.texttospeech("Opening ERP")
        webbrowser.open("https://newerp.kluniversity.in/")
        return "Opening ERP"
    
    elif "lms" in user_data:
        text_to_speech.texttospeech("Opening LMS")
        webbrowser.open("https://lms.kluniversity.in/")
        return "Opening LMS"
    
    elif "instagram" in user_data:
        text_to_speech.texttospeech("Opening Instagram")
        webbrowser.open("https://instagram.com/")
        return "Opening Instagram"
    
    elif "chatgpt" in user_data:
        text_to_speech.texttospeech("Opening ChatGPT")
        webbrowser.open("https://chat.openai.com/")
        return "Opening ChatGPT"
    
    else:
        text_to_speech.texttospeech("Please say again")
        return "Please say again"