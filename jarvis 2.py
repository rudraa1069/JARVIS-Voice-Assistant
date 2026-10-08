from __future__ import with_statement
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import pyautogui
import sys
import time
import operator



engine = pyttsx3.init('sapi5')
voices = engine.getProperty ('voices')
print (voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    print (audio)
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)

        except sr.WaitTimeoutError:
            print("No speech detected.")
            return "none"

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")

    except sr.UnknownValueError:
        speak("Sorry sir, I could not understand that.")
        return "none"

    except sr.RequestError:
        speak("Sorry sir, the speech recognition service is unavailable.")
        return "none"

    return query
def wish():
   hour = int(datetime.datetime.now().hour)

   if hour >=0 and hour <=12:
      speak ("good morning sir ")
   elif hour >12 and hour <18:
      speak ("good afternoon sir")
   else :
      speak ("good evening ")
   speak ("please tell me how can i help you")

if __name__ == "__main__":
   wish()
   while True:
   #if 1 :
       
      query= takecommand().lower() 
      if "stop" in query:
         speak("Thank you sir.")
         sys.exit()
   
      if "open notepad" in query :
         npath ="C:\\WINDOWS\\system32\\notepad.exe"
         os.startfile(npath)

      elif "close notepad" in query:
         os.system("taskkill /f /im notepad.exe")


      elif"open command prompt" in query:
         os.system("start cmd")

      elif "close command prompt" in query:
         os.system("taskkill /f /im cmd.exe")


      elif"open camera" in query :
         cap = cv2.VideoCapture(0)
         while True:
            ret,img =cap.read()
            cv2.imshow('webcam',img)
            k = cv2.waitKey(50)
            if k==27:
               break;
         cap.release()
         cv2.destroyAllWindows()


      elif"play music" in query:
         music_dir = r"C:\Users\Anand Kr Chowdhary\OneDrive\Desktop\song"
         songs = os.listdir(music_dir)
         rd = random.choice(songs)
         os.startfile(os.path.join(music_dir, rd))
         #in SECOND last line we can comment out and in top comment out random variable then in last line in place of rd we can use songs[1] here 1 is the index number of the song

      
       
      elif "ip address" in query:
         ip = get('https://api.ipify.org').text
         speak(f"your IP address is {ip}")


  
      elif "wikipedia" in query:
         speak("searching wikipedia sir give me some time ")
         query=query.replace("wikipedia","")
         results =wikipedia.summary(query , sentences =2)
         speak("according to wikipedia")
         speak(results)
         #print(results)

      elif 'open youtube' in query:
         speak("what you will like to watch ?")
         qrry = takecommand().lower()
         pywhatkit.playonyt(f"{qrry}")

      elif 'close youtube' in query:
         os.system("taskkill /f /im msedge.exe")



      elif "open facebook" in query:
         webbrowser.open ("facebook.com")

      elif "open takeuforward" in query:
         webbrowser.open ("takeuforward.org")

      elif "open instagram" in query:
         webbrowser.open ("instagram.com")

      elif "open xhamster" in query:
         webbrowser.open ("xhamster.desi")

      elif 'close chrome' in query:
         os.system("taskkill /f /im chrome.exe")

      elif 'open google' in query:
         speak("what should I search ?")
         qry = takecommand().lower()
         webbrowser.open(f"{qry}")
         results = wikipedia.summary(qry, sentences=4)
         speak(results)


      elif 'close google' in query:
         os.system("taskkill /f /im msedge.exe")

      elif "send message" in query:
         pywhatkit.sendwhatmsg("+916295204535","this is testing",2,25)


      elif "go to sleep" in query:
        speak(' alright then, I am switching off')
        sys.exit()

      elif "shut down the system" in query:
        os.system("shutdown /s /t 5")

      elif "restart the system" in query:
        os.system("shutdown /r /t 5")

      elif "Lock the system" in query:
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    
      elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S") 
        speak(f"Sir, the time is {strTime}")


      elif "take screenshot" in query:
        speak('tell me a name for the file')
        name = takecommand().lower()
        time.sleep(3)
        img = pyautogui.screenshot() 
        img.save(f"{name}.png") 
        speak("screenshot saved")


      elif "calculate" in query:
        r = sr.Recognizer()
        with sr.Microphone() as source:
          speak("ready")
          print("Listning...")
          r.adjust_for_ambient_noise(source)
          audio = r.listen(source)
        my_string=r.recognize_google(audio)
        print(my_string)
        def get_operator_fn(op):
          return {
         '+' : operator.add,
         '-' : operator.sub,
         'x' : operator.mul,
         'divided' : operator.__truediv__,
          }[op]
        def eval_bianary_expr(op1,oper, op2):
            op1,op2 = int(op1), int(op2)
            return get_operator_fn(oper)(op1, op2)
        speak("your result is")
        speak(eval_bianary_expr(*(my_string.split())))


      elif "volume up" in query:
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
 
      elif "volume down" in query:
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
      elif "mute" in query:
         pyautogui.press("volumemute")


      elif "refresh" in query:
         pyautogui.moveTo(1551,551, 2)
         pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right')
         pyautogui.moveTo(1620,667, 1)
         pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left')
 
      elif "scroll down" in query:
         pyautogui.scroll(1000)


      elif "who created you" in query:
         print('I am created with Python Language by mr anand')
         speak("I am created with Python Language by mr anand")


      elif 'open chrome' in query:
        os.startfile(r'C:\Program Files\Google\Chrome\Application\chrome.exe')
      elif 'maximize this window' in query:
         pyautogui.hotkey('alt', 'space')
         time.sleep(1)
         pyautogui.press('x')
      elif 'google search' in query:
         query = query.replace("google search", "")
         pyautogui.hotkey('alt', 'd')
         pyautogui.write(f"{query}", 0.1)
         pyautogui.press('enter')
     
      elif 'open new window' in query:
         pyautogui.hotkey('ctrl', 'n')
      elif 'open incognito window' in query:
         pyautogui.hotkey('ctrl', 'shift', 'n')
      elif 'minimise this window' in query:
         pyautogui.hotkey('alt', 'space')
         time.sleep(1)
         pyautogui.press('n')
      elif 'open history' in query:
         pyautogui.hotkey('ctrl', 'h')
      elif 'open downloads' in query:
         pyautogui.hotkey('ctrl', 'j')
      elif 'previous tab' in query:
         pyautogui.hotkey('ctrl', 'shift', 'tab')
      elif 'next tab' in query:
         pyautogui.hotkey('ctrl', 'tab')
      elif 'close tab' in query:
         pyautogui.hotkey('ctrl', 'w')
      elif 'close window' in query:
         pyautogui.hotkey('ctrl', 'shift', 'w')
      elif 'clear browsing history' in query:
         pyautogui.hotkey('ctrl', 'shift', 'delete')
    