import speech_recognition as sr
import  random, time


r = sr.Recognizer()

def speach():
   with sr.Microphone() as source:
    print("Говорите...")

    audio = r.listen(source)
    r.adjust_for_ambient_noise(source)
    r_speech = r.recognize_google(audio, language='ru-RU')
    print('Вы сказали: ' + r_speech)
    return r_speech
