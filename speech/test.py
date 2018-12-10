import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()
print(mic.list_microphone_names())
