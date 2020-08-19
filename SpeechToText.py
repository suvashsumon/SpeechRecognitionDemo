# Author : Suvash Kumar
# Website : www.suvashkumar.xyz

import  speech_recognition as sr

recognizer = sr.Recognizer()
print("Talk something......")
with sr.Microphone() as source:
	audio_data = recognizer.record(source, duration=5)
	print("Recongnizing..........")
	text = recognizer.recognize_google(audio_data)
	print("You said : ", text)