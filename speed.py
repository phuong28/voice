import pyttsx3 
import datetime
import  speech_recognition as sr
import webbrowser as wb
speed=pyttsx3.init()
voice=speed.getProperty('voices')# lay giong
speed.setProperty('voice',voice[1].id)# voide[0].id=giong nam
   
def speak(audio):
    print('Cristiano Ronaldo : '+audio)
    speed.say(audio)
    speed.runAndWait()# bat buoc phai co ms chay dc
speak("Hello girl")

def time():
    Time=datetime.datetime.now().strftime("%I : %M : %p ")# thoi gian hien tai
    speak(Time)
def welcome() :
    hour=datetime.datetime.now().hour
    if hour>=6 and hour <12:
        speak(" Good Morning Sir I love you")
    elif hour >=12 and hour <18:
        speak("Good afternoon sir I love you")
    elif hour >=18 and hour <24:
        speak("Good Night sir I love you")
    speak(" I am Cristiano Ronaldo . I miss you so much. How can I help you")   
def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=1 # dung 2 giay sau khi ra lenh moi
        audio=c.listen(source)
    try:
        query=c.recognize_google(audio, language="vi")
        print("NINH PHUONG said:"+ query)
    except sr.UnknownValueError:
        print("Please repeat or typing the command ")
        query=str(input(' Your order is: ')) # neu khong nhan duoc tieng noi thi go lenh vao
    return query   
if __name__=="__main__":
   # welcome()
    while True:
        query=command().lower() # lay thong tin ve dang chu cai thuong
        if "google" in query:
            speak("What should I search boss?")
            search=command().lower()
            url=f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f' Here is your {search} on google')
        if "youtube" in query:
            speak("What should I search boss?")
            search=command().lower()
            url=f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f' Here is your {search} on youtube')
        
