import os
import subprocess
import playsound
import  speech_recognition as sr
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
import cv2
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style
from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as mbox
from pymessager.message import Messager
from googletrans import Translator, LANGUAGES
# from flask import Flask
wikipedia.set_lang('vi')
languages='vi'
root = Tk()
text_area = Text(root, height=26, width=45)
scroll = Scrollbar(root, command=text_area.yview) # thanh cuon
def speak(text):
    print(" Tro ly ao" , text)
    tts=gTTS(text= text, lang=languages, slow=False)
    filename=os.path.dirname(__file__)+"\\robot.mp3"
    tts.save(filename)
    playsound.playsound("robot.mp3", True)
    os.remove(filename)
def command():
    c=sr.Recognizer()
    # c.adjust_for_ambient_noise(source, duration=1)
    with sr.Microphone() as source:
        c.adjust_for_ambient_noise(source, duration=5)
        c.pause_threshold=5 # dung 2 giay sau khi ra lenh moi
        audio=c.listen(source,phrase_time_limit=8)
    try:
        query=c.recognize_google(audio, language="vi-VI" )
        print("người nói :"+ query)
    except sr.UnknownValueError:
        print("Nhập lại đi  ")
        speak("Nhập lại đi tôi không hiểu bạn nói gì")
        query=str(input()) # neu khong nhan duoc tieng noi thi go lenh vao
    return query 
def translate(mystory):
    
    t = Translator().translate(mystory, dest = "en")
    return t.text


def ham_main():
    
    func()
    while True:
        
        query=command().lower()
        text_area.insert(INSERT,"You: "+query+"\n")
        # root.update()
        if translate("google") in translate(query):
            image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))    
            label1 = Label(image=image_1)
            label1.image = image_1
            label1.place(x=7, y=43)
            speak("Bạn muốn tìm gì vậy ạ")
            text_area.insert(INSERT,"Trợ lý ảo: Bạn muốn tìm gì vậy ạ \n")
            root.update()
            time.sleep(3.5)
            search=command().lower()
            text_area.insert(INSERT,"You :"+ search+"\n")
            url=f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f' kết quả tìm kiếm  {search} trên google')
            text_area.insert(INSERT,"Trợ lý ảo:"+f' kết quả tìm kiếm  {search} trên google'+"\n")
            
        elif translate("youtube") in translate(query):
            image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))    
            label1 = Label(image=image_1)
            label1.image = image_1
            label1.place(x=7, y=43)
            speak("Bạn muốn tìm gì vậy ạ")
            text_area.insert(INSERT,"Trợ lý ảo: Bạn muốn tìm gì vậy ạ \n")
            root.update()
            time.sleep(3.5)
            search=command().lower()
            text_area.insert(INSERT,"You :"+ search+"\n")
            url=f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f' kết quả tìm kiếm  {search}  trên youtube')
            text_area.insert(INSERT,"Trợ lý ảo:"+f' kết quả tìm kiếm  {search} trên youtube'+"\n")
        elif translate("music") in translate(query) or translate("nhạc") in translate(query):
            # image_1 = ImageTk.PhotoImage(Image.open("image\\a.gif"))    
            # label1 = Label(image=image_1)
            # label1.image = image_1
            # label1.place(x=7, y=43)
            speak(" Nghe nhạc nhá")
            # root.update()
            # time.sleep(3.5)
            music_dir="C:\\Users\\Admin\\Music"
            songs=os.listdir(music_dir)
            baihat=random.choice(songs)
            doc=" bài hát "+baihat+" đã được mở"
            speak(doc)
            ran=os.startfile(os.path.join(music_dir,baihat))
            
        elif translate("wikipedia") in translate(query):
            image_1 = ImageTk.PhotoImage(Image.open("image\\hacker1.jpg"))    
            label1 = Label(image=image_1)
            label1.image = image_1
            label1.place(x=7, y=43)
            speak("Bạn tìm gì ạ")
            text_area.insert(INSERT,"Trợ lý ảo: Bạn muốn tìm gì vậy ạ \n")
            root.update()
            time.sleep(3.5)
            search=command().lower()
            text_area.insert(INSERT,"You :"+ search+"\n")
            res="kết quả tìm kiếm "+search +" trên wikipedia đã được mở"
            url=f"https://vi.wikipedia.org/wiki/{search}"
            text_area.insert(INSERT,"Trợ lý ảo :"+ res+"\n")
            wb.get().open(url)
            
        elif translate("văn bản") in translate(query):
            speak("Word của bạn vừa được mở")
            text_area.insert(INSERT,"Trợ lý ảo : Word của bạn vừa được mở\n")
            os.startfile(r"C:\\Program Files (x86)\\Microsoft Office\\Office16\\WINWORD.EXE")
        elif translate("power point") in translate(query):
            speak("powerpoint của bạn vừa được mở")
            text_area.insert(INSERT,"Trợ lý ảo :powerpoint của bạn vừa được mở\n")
            os.startfile(r"C:\\Program Files (x86)\\Microsoft Office\\Office16\\POWERPNT.EXE")
        elif translate("excel") in translate(query):
            speak("excel của bạn vừa được mở")
            text_area.insert(INSERT,"Trợ lý ảo :excel của bạn vừa được mở\n")
            os.startfile(r"C:\\Program Files (x86)\\Microsoft Office\\Office16\\EXCEL.EXE")
        elif translate("onenote") in translate(query):
            speak("one note của bạn vừa được mở")
            text_area.insert(INSERT,"Trợ lý ảo :one note của bạn vừa được mở\n")
            os.startfile(r"C:\\Program Files (x86)\\Microsoft Office\\Office16\\ONENOTE.EXE")
        elif translate("out look") in translate(query):
            speak("out look của bạn vừa được mở")
            text_area.insert(INSERT,"Trợ lý ảo :out look của bạn vừa được mở\n")
            os.startfile(r"C:\\Program Files (x86)\\Microsoft Office\\Office16\\OUTLOOK.EXE")
        elif translate("đổi ảnh nền") in translate(query):
            image_1 = ImageTk.PhotoImage(Image.open("image\\hacker1.jpg"))    
            label1 = Label(image=image_1)
            label1.image = image_1
            label1.place(x=7, y=43)
            
            root.update()
            time.sleep(3.5)
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
            speak("ảnh nền máy tính của bạn vừa được thay đổi")
            text_area.insert(INSERT,"Trợ lý ảo :ảnh nền máy tính của bạn vừa được thay đổi\n")
        elif translate("thời tiết") in translate(query):
            image_1 = ImageTk.PhotoImage(Image.open("image\\thoitiet1.jpg"))    
            label1 = Label(image=image_1)
            label1.image = image_1
            label1.place(x=7, y=43)
            
            speak("bạn muốn xem thời tiết ở đâu")
            text_area.insert(INSERT,"Trợ lý ảo :bạn muốn xem thời tiết ở đâu\n")
            root.update()
            time.sleep(3.5)
            url="http://api.openweathermap.org/data/2.5/weather?"
            city=command().lower()
            text_area.insert(INSERT,"You: "+city+"\n")
            if not city:
                pass
            api_key="8eaefe86e0342339fc1f2c45400173a3"
            call_url=url+"appid="+api_key+"&q="+city
            respone=requests.get(call_url)
            data=respone.json()
            if data["cod"]!="404":
                city_res=data['main']
                current_temperaturr=city_res["temp"]
                t=int(current_temperaturr/10)
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
                Nhiệt độ trung bình là { t} độ C
                áp suất không khí {current_pressure} héc tơ Pascal
                độ ẩm là {current_humidity}%
                Trời hôm nay quang mây. Dự báo mưa rải rác một số nơi."""
                dcm="chào bạn, bạn muốn xem thời tiết ở"+city+"để ý nghe nhé"
                speak(dcm)
                speak(content)
                text_area.insert(INSERT,"Trợ lý ảo :"+dcm+"\n")
                text_area.insert(INSERT,"Trợ lý ảo :"+content+"\n")
                
                time.sleep(15)

            else:
                speak("Không tìm thấy địa chỉ của bạn")
                text_area.insert(INSERT,"Trợ lý ảo :Không tìm thấy địa chỉ của bạn \n")
        elif translate("bản đồ") in translate(query):
            image_1 = ImageTk.PhotoImage(Image.open("image\\hacker1.jpg"))    
            label1 = Label(image=image_1)
            label1.image = image_1
            label1.place(x=7, y=43)
            
            
            speak("bạn tìm gì ạ")
            text_area.insert(INSERT,"Trợ lý ảo :bạn tìm gì ạ \n")
            root.update()
            time.sleep(3.5)
            search=command().lower()
            text_area.insert(INSERT,"You: "+search+"\n")
            speak("bạn muốn tìm địa chỉ"+search)
            text_area.insert(INSERT,"Trợ lý ảo :bạn muốn tìm địa chỉ"+search +"\n")
            query=query.replace("bản đồ",search)
            location=query
            
            wb.open("https://www.google.com/maps/place/"+location+"")
        elif translate("thời gian") in translate(query):
            image_1 = ImageTk.PhotoImage(Image.open("image\\thoigian.jpg"))    
            label1 = Label(image=image_1)
            label1.image = image_1
            label1.place(x=7, y=43)
            
            now = datetime.datetime.now()
            speak("Bạn muốn ngày hay giờ ạ")
            text_area.insert(INSERT,"Trợ lý ảo :bạn muốn xem ngày hay giờ ạ \n")
            text=command().lower()
            text_area.insert(INSERT,"You: "+text+"\n")
            root.update()
            time.sleep(3)
            if translate("giờ") in translate(text):
                f='Bây giờ là %d giờ %d phút' % (now.hour, now.minute)
                speak(f)
                text_area.insert(INSERT,"Trợ lý ảo :"+f+"\n")
            elif translate("ngày") in translate(text):
                f='Hôm nay là ngày %d tháng  %d năm' % (now.date, now.month,now.year)
                speak('Hôm nay là ngày %d tháng  %d năm' % (now.date, now.month,now.year))
                text_area.insert(INSERT,"Trợ lý ảo :"+f+"\n")
            else:
                speak("mình chưa hiểu ý của bạn. bạn nói lại được không?")
                text_area.insert(INSERT,"Trợ lý ảo :mình chưa hiểu ý của bạn. bạn nói lại được không?"+"\n")
        elif translate("tạm biệt ") in translate(query):
            speak("tạm biệt bạn nhé")
            exit()
        elif translate("đọc báo hôm nay") in translate(query):
            speak("bạn muốn đọc gì nào")
            text_area.insert(INSERT,"Trợ lý ảo :bạn muốn đọc gì nào"+"\n")
            queue=command().lower()
            text_area.insert(INSERT,"You: "+queue+"\n")
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
        elif translate("gửi thư") in translate(query):
            speak("Bạn gửi email cho ai nhỉ")
            text_area.insert(INSERT,"Trợ lý ảo :Bạn gửi email cho ai nhỉ"+"\n")
            recipient=command().lower()
            text_area.insert(INSERT,"You: "+recipient+"\n")
            if "đủ" in recipient:
                speak("Nội dung bạn muốn gửi là gì")
                text_area.insert(INSERT,"Trợ lý ảo :Nội dung bạn muốn gửi là gì"+"\n")
                content=command().lower()
                text_area.insert(INSERT,"You: "+content+"\n")
                mail=smtplib.SMTP('smtp.gmail.com',587)
                mail.ehlo()
                mail.starttls()
                mail.login('ninhphuong2k1nb@gmail.com','2810phuong')
                mail.sendmail('ninhphuong2k1nb@gmail.com','dunguyendinh2001@gmail.com',content.encode('utf-8'))
                mail.close()
                speak("Email của bạn vừa được gửi . bạn check lại mail nhé")
                text_area.insert(INSERT,"Trợ lý ảo :Email của bạn vừa được gửi . bạn check lại mail nhé"+"\n")
            else: 
                speak("Nói lại đi bạn . Tôi không hiểu")
                text_area.insert(INSERT,"Trợ lý ảo :Nói lại đi bạn . Tôi không hiểu "+"\n")
        elif translate("khóa tạm thời") in translate(query):
            speak("bạn thích khóa à")
            ctypes.windll.user32.LockWorkStation()
            exit()
        elif translate("mở phép tính") in translate(query):
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
            exit()
        elif translate("khởi động") in translate(query):
            subprocess.call(["shutdown", "/r"])
        elif translate("máy ảnh") in translate(query):
            cam = cv2.VideoCapture(0)

            img_counter = 0
            while True:
                ret, frame = cam.read()
                if not ret:
                    speak("lỗi rồi")
                    break
                cv2.imshow("Camera", frame)
                k = cv2.waitKey(1)
                if k==113:# nhấn phím q
                    speak("Ứng dụng vừa được đóng")
                    text_area.insert(INSERT,"Trợ lý ảo :Ứng dụng vừa được đóng "+"\n")
                    break
                elif k==32:
                    img_name = "picture_{}.png".format(img_counter)
                    cv2.imwrite(img_name, frame)
                    speak("Ảnh vừa được chụp")
                    text_area.insert(INSERT,"Trợ lý ảo :ảnh vừa đưọc chụp"+"\n")
                img_counter += 1     
            cam.release()
            cam.destroyAllWindows()
        text_area.insert(INSERT,"_____________________________________________")
        query=""
        time.sleep(7)
def func():
    image1 = Image.open("image\\trolyao.jpg")
    image_1 = ImageTk.PhotoImage(image1)    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    speak("Chào bạn, bạn tên là gì nhỉ")
    text_area.insert(INSERT,"tro ly ao "+"Chào bạn, bạn tên là gì nhỉ"+"\n")
    query=command().lower()
    
    txt="chào bạn  "+query
   
    speak(txt)
    text_area.insert(INSERT,"tro ly ao "+txt+"\n")
    speak(" tôi là trợ lý ảo ")
    text_area.insert(INSERT,"tro ly ao "+"tôi là trợ lý ảo\n")
    speak( "tôi   có thể giúp bạn các chức năng sau")
    text_area.insert(INSERT,"tro ly ao "+"tôi   có thể giúp bạn các chức năng sau\n")
    speak("1.Mở trình duyệt web và tìm kiếm")
    text_area.insert(INSERT,"tro ly ao "+"1.Mở trình duyệt web và tìm kiếm\n")
    speak("2.Đọc thời gian hiện tại")
    text_area.insert(INSERT,"tro ly ao "+"2.Đọc thời gian hiện tại\n")
    speak("3.Mở nhạc trên laptop của bạn")
    text_area.insert(INSERT,"tro ly ao "+"3.Mở nhạc trên laptop của bạn\n")
    speak("4.Tìm kiếm thông tin trên wikipedia")
    text_area.insert(INSERT,"tro ly ao "+"4.Tìm kiếm thông tin trên wikipedia\n")
    speak("5.Mở các application trên máy bạn")
    text_area.insert(INSERT,"tro ly ao "+"5.Mở các application trên máy bạn\n")
    speak("6.Thay đổi ảnh nền máy bạn")
    text_area.insert(INSERT,"tro ly ao "+"6.Thay đổi ảnh nền máy bạn\n")
    speak("7.Tìm kiếm thông tin thời tiết của thành phố")
    text_area.insert(INSERT,"tro ly ao "+"7.Tìm kiếm thông tin thời tiết của thành phố\n")
    speak("8.Tra map")
    text_area.insert(INSERT,"tro ly ao "+"8.Tra map\n")
    speak("9.gửi email")
    text_area.insert(INSERT,"tro ly ao "+"9.gửi email\n")
    speak("10.Khởi động và tắt  máy bạn")
    text_area.insert(INSERT,"tro ly ao "+"10.Khởi động và tắt  máy bạn\n")
    speak("11. Đọc báo hôm nay")
    text_area.insert(INSERT,"tro ly ao "+"11. Đọc báo hôm nay\n")
    speak("12.Mở Webcam")
    text_area.insert(INSERT,"tro ly ao "+"12.Mở Webcam\n")
    root.update()
    
    time.sleep(5)
    
#Note 2
def color():
    mylist = ["#009999","black","green","grey","blue","orange","#cc0099","#00ff00","brown"]
    aa=random.choice(mylist)
    text_area.tag_add("here", "1.0", "100000.0")
    text_area.tag_config("here", background = aa)
    root.update()
#Note 3
def color1():
    mylist1 = ["yellow","#0000ff","white","#00ff00","black"]
    bb=random.choice(mylist1)
    text_area.tag_add("here", "1.0", "100000.0")
    text_area.tag_config("here",foreground = bb)
    root.update()
#Note 4
def info():
    mbox.showinfo("Giới thiệu", "-Nhấn Micro để bắt đầu thực hiện nói với AI.\n-Nhấn Làm mới để xóa toàn bộ cuộc trò chuyện.\n-Bạn có thể thay đổi màu nền hoặc màu chữ ngẫu nhiên.\n-Tiếng Pip xuất hiện là lúc AI đang nghe bạn nói.\n-Nói 'dừng lại' để tạm hoãn cuộc trò chuyện. \n-Nhấn Thoát để tắt chương trình.")

def r_set():
    image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    text_area.delete("1.0", "1000000000.0")



class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent) 
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("Trợ lí ảo")
        self.style = Style()
        self.style.theme_use("default")
        
        scroll.pack(side=RIGHT, fill=Y)
        text_area.configure(yscrollcommand=scroll.set)
        text_area.pack(side=RIGHT)

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        self.pack(fill=BOTH, expand=True)

        image3 = Image.open("image\\micro.png")
        image_3 = ImageTk.PhotoImage(image3)  
        label = Label(image=image_3)
        label.image = image_3
        label.place(x=430, y=477)

        closeButton = Button(self, text="Thoát",command = exit,width=10,fg="white", bg="#009999",bd=3)
        closeButton.pack(side=RIGHT, padx=11, pady=10)
        okButton = Button(self, text="Micro",command = ham_main,width=10,fg="white", bg="#009999",bd=3)
        okButton.pack(side=RIGHT, padx=11, pady=10)
        doimau = Button(self,text="Đổi màu nền",command = color,width=10,fg="white", bg="#009999",bd=3)
        doimau.pack(side=RIGHT,padx=11, pady=10)
        doimau = Button(self,text="Đổi màu chữ",command = color1,width=10,fg="white", bg="#009999",bd=3)
        doimau.pack(side=RIGHT,padx=11, pady=10)
        thongtin = Button(self,text="Giới thiệu",command = info,width=10,fg="white", bg="#009999",bd=3)
        thongtin.pack(side=RIGHT,padx=11, pady=10)
        lammoi = Button(self,text="Làm mới",command = r_set,width=10,fg="white", bg="#009999",bd=3)
        lammoi.pack(side=RIGHT,padx=11, pady=10)

        # self.pack(fill=BOTH, expand=1)   
        # Style().configure("TFrame", background="#333")
    
        image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))    
        label1 = Label(self, image=image_1)
        label1.image = image_1
        label1.place(x=7, y=43)

        l = Label(root, text='Lịch sử trò chuyện', fg='White', bg='blue')
        l.place(x = 750, y = 10, width=120, height=25)
        l1 = Label(root, text='nền ảnh', fg='yellow', bg='black')
        l1.place(x = 250, y = 11, width=120, height=25)

root.geometry("1000x510+350+50")
root.resizable(False, False)
app = Example(root)
root.mainloop()
        
