import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone(device_index=3)
with mic:
    audio = r.listen(mic)


r.re