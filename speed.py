import os
import subprocess
import playsound
import speech_recognition as sr
import time
import sys
import ctypes
import wikipedia
import datetime
import json
import re
import random
import smtplib
import requests
import urllib
import urllib.request as urllib2
import webbrowser as wb
from time import sleep, strftime
from gtts import gTTS
from wikipedia.wikipedia import languages
import win32com.client as wincl
import operator
import subprocess

wikipedia.set_lang('vi')
languages='vi'
def speak(text):
    print(" Tro ly ao" , text)
    tts=gTTS(text= text, lang=languages, slow=False)
    filename=os.path.dirname(__file__)+"\\robot.mp3"
    tts.save(filename)
    playsound.playsound("robot.mp3", True)
    os.remove(filename)
def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=2 # dung 1 giay sau khi ra lenh moi
        audio=c.listen(source,phrase_time_limit=3)
    try:
        query=c.recognize_google(audio, language="vi-VI" )
        print("người nói :"+ query)
    except sr.UnknownValueError:
        print("Nhập lại đi cưng ")
        speak("Nhập lại đi")
        query=str(input()) # neu khong nhan duoc tieng noi thi go lenh vao
    return query 

if __name__=="__main__":
    speak("Chào cưng, cưng tên gì nhỉ")
    #query=command().lower()
    
    #txt="chào cưng "+query
    #speak(txt)

    #speak(" tôi là thợ sửa ống nước")
    #speak("Tôi có thể giúp cưng các chức năng sau")
    #speak("1.Mở trình duyệt web và tìm kiếm")
    #speak("2.Đọc thời gian hiện tại")
    #speak("3.Mở nhạc trên laptop của cưng")
    #speak("4.Tìm kiếm thông tin trên wikipedia")
    #speak("5.Mở các application trên máy cưng")
    #speak("6.Thay đổi ảnh nền máy cưng")
    #speak("7.Tìm kiếm thông tin thời tiết của thành phố")
    #speak("8.Tra map")
    #speak("9.gửi email")
    #speak("10.Khởi động và tắt  máy cưng")
    #speak("11. Đọc báo hôm nay")
    while True:
        query=command().lower()
        if "google" in query:
            speak("Bạn muốn tìm gì vậy cưng")
            search=command().lower()
            url=f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f' kết quả tìm kiếm  {search} trên google')
        elif "youtube" in query:
            speak("Bạn muốn tìm gì vậy cưng")
            search=command().lower()
            url=f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f' kết quả tìm kiếm  {search} trên youtube')
        elif "music" in query or "nhạc" in query:
            speak(" Nghe nhạc nhá")
            music_dir="C:\\Users\\Admin\\Music"
            songs=os.listdir(music_dir)
            baihat=random.choice(songs)
            doc=" bài hát "+baihat+" đã được mở"
            speak(doc)
            ran=os.startfile(os.path.join(music_dir,baihat))
            exit()
        elif "wikipedia" in query:
            speak("Cưng tìm gì ạ")
            search=command().lower()
            res="kết quả tìm kiếm "+search +" trên wikipedia đã được mở"
            url=f"https://vi.wikipedia.org/wiki/{search}"
            wb.get().open(url)
            exit()
        elif "văn bản" in query:
            speak("Word của cưng vừa được mở")
            os.startfile(r"C:\\Program Files (x86)\\Microsoft Office\\Office16\\WINWORD.EXE")
        elif "ba boi" in query:
            speak("powerpoint của cưng vừa được mở")
            os.startfile(r"C:\\Program Files (x86)\\Microsoft Office\\Office16\\POWERPNT.EXE")
        elif "excel" in query:
            speak("excel của cưng vừa được mở")
            os.startfile(r"C:\\Program Files (x86)\\Microsoft Office\\Office16\\EXCEL.EXE")
        elif "oăn nốt" in query:
            speak("one note của cưng vừa được mở")
            os.startfile(r"C:\\Program Files (x86)\\Microsoft Office\\Office16\\ONENOTE.EXE")
        elif "ao lúc" in query:
            speak("out look của cưng vừa được mở")
            os.startfile(r"C:\\Program Files (x86)\\Microsoft Office\\Office16\\OUTLOOK.EXE")
        elif "đổi ảnh nền" in query:
            api_key="Nq3RP19RwurdZXUVtmGk661Tv3c3sih1ogOrxKbM6Ls"
            url='http://api.unsplash.com/photos/random?client_id='+api_key
            f=urllib2.urlopen(url)
            json_string=f.read()
            f.close()
            parsed_json=json.loads(json_string)
            photo=parsed_json['urls']['full']
            urllib2.urlretrieve(photo,r"C:\Users\Admin\Downloads\image_change.png")
            image=os.path.join(r"C:\Users\Admin\Downloads\image_change.png")
            ctypes.windll.user32.SystemParametersInfoW(20,0,image,3)
            speak("ảnh nền máy tính của cưng vừa được thay đổi")
        elif "thời tiết" in query:
            speak("Cưng muốn xem thời tiết ở đâu")
            url="http://api.openweathermap.org/data/2.5/weather?"
            city=command().lower()
            if not city:
                pass
            api_key="8eaefe86e0342339fc1f2c45400173a3"
            call_url=url+"appid="+api_key+"&q="+city
            respone=requests.get(call_url)
            data=respone.json()
            if data["cod"]!="404":
                city_res=data['main']
                current_temperaturr=city_res["temp"]
                current_pressure=city_res["pressure"]
                current_humidity = city_res["humidity"]
                suntime = data["sys"]
                sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
                sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
                wthr = data["weather"]
                weather_description = wthr[0]["description"]
                now = datetime.datetime.now()
                content = f"""
                Hôm nay là ngày {now.day} tháng {now.month} năm {now.year}
                Mặt trời mọc lúc {sunrise.hour} giờ  {sunrise.minute} phút
                Mặt trời lặn lúc {sunset.hour} giờ {sunset.minute} phút
               Nhiệt độ trung bình là { current_temperaturr} độ C
                áp suất không khí {current_pressure} héc tơ Pascal
                độ ẩm là {current_humidity}%
                Trời hôm nay quang mây. Dự báo mưa rải rác một số nơi."""
                dcm="chào cưng, cưng muốn xem thời tiết ở"+city+"để ý nghe nhé"
                speak(dcm)
                speak(content)

                time.sleep(20)

            else:
                speak("Không tìm thấy địa chỉ của bạn")
        elif "bản đồ" in query:
            speak("cưng tìm gì ạ")
            search=command().lower()
            speak("cưng muốn tìm địa chỉ"+search)
            query=query.replace("bản đồ",search)
            location=query
            
            wb.open("https://www.google.com/maps/place/"+location+"")
        elif "thời gian" in query:
            now = datetime.datetime.now()
            text=command().lower()
            if "giờ" in text:
                speak('Bây giờ là %d giờ %d phút' % (now.hour, now.minute))
            elif "ngày" in text:
                speak("Hôm nay là ngày %d tháng %d năm %d" %
                (now.day, now.month, now.year))
            else:
                speak("mình chưa hiểu ý của cưng. cưng nói lại được không?")
        elif "tạm biệt bé" in query:
            speak("tạm biệt cưng nhé")
            exit()
        elif "đọc báo hôm nay" in query:
            speak("Cưng muốn đọc gì nào")
            queue=command().lower()
            params={
                'apiKey':'b4f8a816a72e455cba7ded1a329b0b9f',
                "q":queue,
            }
            api_result=requests.get('http://newsapi.org/v2/top-headlines?',params)
            api_response=api_result.json()
            print("Tin tức")
            for number,result in enumerate(api_response['articles'],start=1):
                print(f"""Tin{number}:\n Tiêu đề: {result['title']}\n Trích dẫn: {result['description']}\n Link:{result['url']}""")
                if number<=3:
                    wb.open(result['url'])
        elif "gửi thư" in query:
            speak("Bạn gửi email cho ai nhỉ")
            recipient=command().lower()
            if "đủ" in recipient:
                speak("Nội dung bạn muốn gửi là gì")
                content=command().lower()
                mail=smtplib.SMTP('smtp.gmail.com',587)
                mail.ehlo()
                mail.starttls()
                mail.login('ninhphuong2k1nb@gmail.com','2810phuong')
                mail.sendmail('ninhphuong2k1nb@gmail.com','dunguyendinh2001@gmail.com',content.encode('utf-8'))
                mail.close()
                speak("Email của cưng vừa được gửi . Cưng check lại mail nhé")
            else: speak("Nói lại đi cưng . Chị không hiểu")
        elif "khóa tạm thời"    in query:
            speak("cưng thích khóa à")
            ctypes.windll.user32.LockWorkStation()
            exit()
        elif "mở phép tính" in query:
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
            exit()
        elif "khởi động" in query:
            subprocess.call(["shutdown", "/r"])
        
