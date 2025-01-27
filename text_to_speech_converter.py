'''import gtts
from playsound import playsound
l=gtts.gTTS("Hello world")
l.save("sunay_dj.mp3")
playsound("sunay_dj.mp3")'''
import pyttsx3
engine=pyttsx3.init()
engine.setProperty('rate',150)
engine.setProperty('volume',1)
text='welcome to my world'
engine.say(text)
engine.runAndWait()
