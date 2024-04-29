import text_to_speech
import speech_to_text
import datetime
import webbrowser

def Action(data):
    user_data = data.lower()
#It makes all the words as lower case from the user input
    if "what is your name" in user_data :
        text_to_speech.text_to_speech("My name is allen")
        return "My name is allen"
    
    elif "hello" in user_data or "hye" in user_data:
        text_to_speech.text_to_speech("hey,sir how can i help you")
        return "hey, sir how can i help you"

    elif "love you allen" in user_data:
         text_to_speech.text_to_speech("love you three thousand sir")
         return "love you three thousand sir"

    elif "tell about yourself" in user_data:
        text_to_speech.text_to_speech("Myself allen I am an AI chat bot and I am here to assist you sir")
        return "Myself allen I am a AI chat bot and I am here to assist you sir"
    
    elif "good morning" in user_data:
        text_to_speech.text_to_speech("good morning sir")
        return "good morning sir"
    
    elif "what is the time" in user_data:
        current_time = datetime.datetime.now() 
        Time = "current time is" +str(current_time.hour) + "Hour :" + str(current_time.minute) + "Minute :"
        text_to_speech.text_to_speech(Time)
        return Time
     
    elif "shutdown" in user_data:
         text_to_speech.text_to_speech("ok sir ,turning down system")
         return "ok sir ,turning down system"
     
    elif "play music allen" in user_data:
        webbrowser.open("https://spotify.com/")
        text_to_speech.text_to_speech("playing music in spotify,sir")
        return "playing music in spotify,sir"
    
    elif "open youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech("opening youtube,sir")
        return "opening youtube,sir"
    
    elif "open google" in user_data:
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speech("accessing to google,sir")   
        return "accessing to google,sir" 
    
    elif "open chatbot" in user_data:
        webbrowser.open("https://chat.openai.com/")
        text_to_speech.text_to_speech("chatbot is ready,sir")
        return "chatbot is ready,sir"
    
    elif "open whatsapp" in user_data:
        webbrowser.open("https://web.whatsapp.com/")
        text_to_speech.text_to_speech("accessing whatsApp ,sir")
        return  "accessing whatsApp ,sir"
    
    elif "open maps" in user_data:
        webbrowser.open("https://www.google.co.in/maps")
        text_to_speech.text_to_speech("accessing maps,sir")
        return  "accessing maps,sir"
    
    elif "get latest news about stocks" in user_data:
        webbrowser.open("https://www.nseindia.com/")
        text_to_speech.text_to_speech("checking stockmarket,sir")
        return  "checking stockmarket,sir"
    
    elif "create a webmeeting allen" in user_data:
        webbrowser.open("https://live.zoom.us/")
        text_to_speech.text_to_speech("getting a meeting ready,sir")
        return  "getting a meeting ready ,sir"
    
     
    elif "any reminders left allen" in user_data:
        webbrowser.open("https://calendar.google.com/")
        text_to_speech.text_to_speech("let me check,sir")
        return  "let me check,sir"
    
    elif "access my mobile" in user_data:
        webbrowser.open("https://web.airdroid.com/")
        text_to_speech.text_to_speech("logging into your mobile sir")
        return  "logging into your mobile sir"
    
    elif "is there any new mails for me" in user_data:
        webbrowser.open("https://mail.google.com/")
        text_to_speech.text_to_speech("checking your mail account, sir")
        return  "checking your mail account,sir"
    
    else:
        text_to_speech.text_to_speech("I'm not able to undrstand ,sir")
        return  "I'm not able to understand ,sir"