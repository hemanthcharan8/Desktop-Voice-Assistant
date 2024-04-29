#import a library called pyttsx3 to convert text to speech
import pyttsx3
def text_to_speech(text):
   engine= pyttsx3.init()
   rate=engine.getProperty("rate")
#set the rate of the engine to a lower value
   engine.setProperty("rate ","rate-80")
#use engine to speak the input text 
   engine.say(text)
   engine.runAndWait()
text_to_speech("Hello")