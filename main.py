import speech_recognition as sr
import win32com.client
import pythoncom
import webbrowser
import datetime
import openai
from config import apikey
import os
import random
import time
from weather_tell import *
from playsound import playsound
from alarm_clock_t import alarm, CLEAR,CLEAR_AND_RETURN
from sound_recorder import *



def speech_to_number(speech_numeral):
    numeral_mapping = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12, 
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20
    }

    return numeral_mapping.get(speech_numeral.lower(), None)


    


    

def p_time(time):
   return time.strftime('%I:%M %p')

def activate_jarvis():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 2
        audio = r.listen(source,phrase_time_limit=5)
        try: 
         #print("Recognizing....")
         query = r.recognize_google(audio, language="en-us")
         #print(f"user said: {query}\n")
         return query
        except Exception as e:
            return "Cant Recognise . Please try again!"



chatStr = ""
# https://youtu.be/Z3ZAJoi4x6Q
def chat(text):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"BOSS : {text}\n JARVIS: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

    
    

speaker = win32com.client.Dispatch("SAPI.SpVoice")


def say(s):
  speaker.speak(s)
    
    
def takecommand():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 2
        audio = r.listen(source,phrase_time_limit=5)
        try: 
         print("Recognizing....")
         query = r.recognize_google(audio, language="en-in")
         #print(f"user said: {query}\n")
         return query
        except Exception as e:
            return "Cant Recognise . Please try again!"
    
if __name__ == '__main__':
    say('Hi there, Iam Jarvis. How can I Help You Today')
    count =True
    react = False
    while count==True:
     print("\n\n")
     print('listening....')
     text = takecommand()
     i=0 
     j=0
     #sites = [["youtube","https://youtube.com"],["wikipedia","https://wikipedia.com"],["Gmail","https://gmail.com"],["facebook","https://facebook.com"]]
     #for i in range(4):   
     if "open youtube".lower() in text.lower():
          say(f"opening youtube sir")
          webbrowser.open("https://youtube.com")
     elif "open gmail".lower() in text.lower():
          say(f"opening gmail sir")
          webbrowser.open("https://gmail.com")
     elif "open wikipedia".lower() in text.lower():
          say(f"opening wikipedia sir")
          webbrowser.open("https://wikipedia.com")
     elif "open facebook".lower() in text.lower():
          say(f"opening facebook sir")
          webbrowser.open("https://facebook.com")
     elif "weather today".lower() in text.lower():
          say(f"current temperature is {temp_celsius:.2f} degree celsius in {CITY}")
          say(f"Feels like {feels_like_celsius:.2f} degree celsius ")
          say(f"current wind speed in {CITY} is {wind_speed:.2f} meters per second")
          say(f"Humididty is {humidity:.2f}% ")
          say(f"Today {description} can be seen")
          say(f"Sun rises in {CITY} at {sunrise_time} local time")
          say(f"Sun set in {CITY} at {sunset_time} local time")
     elif "Set alarm".lower() in text.lower(): 
          say(f"how many minutes you want to set the alarm for ")
          mins_to_wait = activate_jarvis()
          speech_numeral = mins_to_wait
          minutes_to_wait = speech_to_number(speech_numeral)
          print(type(minutes_to_wait))
          say(f"how many seconds you want to set the alarm for ")
          secs_to_wait = activate_jarvis()
          speech_numeral = secs_to_wait
          seconds_to_wait = speech_to_number(speech_numeral)    
          total_time_in_seconds = minutes_to_wait*60 + seconds_to_wait
          say(f"what is the purpose of adding this Alarm")
          reason = activate_jarvis()
          say(f"The Alarm has been set for {mins_to_wait} minutes and {secs_to_wait} seconds")
          alarm(total_time_in_seconds)
          say(f"Sir the purpose of this Alarm was to remind you about {reason}")        
     elif "sleep".lower() in text.lower():
         count = False
         say("See You Soon Boss\n\n")
         print("Sleeping :)")
         react=False
         while react==False:
          reactivate = activate_jarvis()
          if "wake up Jarvis".lower() in reactivate.lower():
            count = True
            react = True 
            say("Yes Boss")           
     elif "the time".lower() in text.lower():
         '''strfTime = datetime.datetime.now().strftime("%H:%M:%S")
         say(f"sir the time is : {strfTime}")'''
         time = datetime.datetime.now()
         time_format = p_time(time)
         say(f"Current Time is: {time_format}")
     #elif"set alarm".lower() in text.lower():
         #alarm_clock()
     elif "start recording".lower() in text.lower():
         
         say(f"what would be the name of this file")
         name_of_file = activate_jarvis()
         say(f"what would be the duration of this recording in minutes")
         duration_in_minuts = activate_jarvis()
         speech_numeral = duration_in_minuts
         minutes_of_recording =speech_to_number(speech_numeral)
         total_seconds= minutes_of_recording*60
         say(f" Sir the recording has been started ")
         file_path = "C:\\Users\\TEST\\OneDrive\\Desktop\\century\\recorded_audios\\"
         start_voice_recording(file_path + name_of_file+".wav",total_seconds)
         say("sir this recording has been finished")
         
     elif "created you".lower() in text.lower():
         say("Mister Akash which is you Boss")
     elif "Using artificial intelligence".lower() in text.lower():
         ai(prompt=text)

     elif "Jarvis Quit".lower() in text.lower():
         exit()

     elif "reset chat".lower() in text.lower():
         chatStr = ""
         say("The chat has been reset")

     else:
         print("Chatting...\n|********************RECENT CHAT*************************|\n")
         chat(text)
         
     
     
         
     #say(text)
        