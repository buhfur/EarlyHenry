import win32com.client as wincl
import speech_recognition as sr

speak = wincl.Dispatch("SAPI.SpVoice")

r = sr.Recognizer()


with sr.Microphone() as source:
    audio = r.listen(source)
    text = r.recognize_google(audio)

    print("you said {}".format(text))
