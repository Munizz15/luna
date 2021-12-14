# Our main file.

import speech_recognition as sr

# cria o reconhecedor.
r = sr.Recognizer()

# Iniciar microfone para captura
with sr.Microphone() as source:
	audio = r.listen(source) # define microfone como entrada de audio

	print(r.recognize_google(audio))

