#import the speech recongnition library and assign it as sr.
import speech_recognition as sr
def speech_to_text():
   r= sr.Recognizer()
   with sr.Microphone() as source:
#listen to audio input from the microphone
    audio = r.listen(source)
    try:
#intialize an empty string variable to store the voice data
     voice_data=""
#use the recognizer object to convert the audio input to text
     voice_data = r.recognize_google(audio) 
     print(voice_data)     
     return voice_data
#if the speech recognition service is unable to recognize the spoken language,print an error message
    except sr.UnknownValueError:      
        print("error")
    except sr.RequestError:
        print("RequestError") 
           
speech_to_text()     
        
