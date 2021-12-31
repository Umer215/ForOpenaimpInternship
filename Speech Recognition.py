import speech_recognition as sr
a=sr.Recognizer()

with sr.Microphone() as source:
    print("What do you want to search\n")
    audio=a.listen(source)

print('opening : ' + r.recognize_google(audio))
