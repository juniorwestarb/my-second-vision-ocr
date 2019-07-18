import speech_recognition as spech
from gtts import gTTS
from playsound import playsound

def criar_audio(audio):
	create = gTTS(audio, lang='pt-br')
	create.save('audios/deteccao.mp3')
	playsound('audios/deteccao.mp3')


def ouvir():
	microfone = spech.Recognizer()
	with spech.Microphone() as source:
		microfone.adjust_for_ambient_noise(source)
		audio = microfone.listen(source)

	try:
		frase = microfone.recognize_google(audio, language='pt-BR')

	except spech.UnkownValueError:
		print("Não entendi")

	return frase

#reconhecimento = ouvir()
#cria_audio(reconhecimento)
