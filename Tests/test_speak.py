#from Voice import Voice
import speech_recognition as sr
import win32com.client as wincl

r = sr.Recognizer()

def test_speak():

    with sr.Microphone() as source:
        print("say anything to test the speech")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print(text)



def test_voice():
    #initializes the engine to render text
    speak = wincl.Dispatch("SAPI.SpVoice")
    try:

        speak.Speak("this is a test. the quick brown fox, jumped over the-lazy dog.")
    except Exception as e:
        print(e)
        print("voice didnt work")

test_speak()
test_voice()
