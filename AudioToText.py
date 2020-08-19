# Author : Suvash Kumar
# Website : www.suvashkumar.xyz

import speech_recognition as sr

recognizer = sr.Recognizer()
audio_file = "speech.wav"

with sr.AudioFile(audio_file) as source:
	audio_data = recognizer.record(source)
	print("Recognizing this speech ......")
	text = recognizer.recognize_google(audio_data)
	print("Content of this audio : ",text)